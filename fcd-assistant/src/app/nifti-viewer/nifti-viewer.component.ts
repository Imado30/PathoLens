import { Component, OnInit, AfterViewInit, OnDestroy, ViewChild, ElementRef } from '@angular/core';
import { Niivue, DRAG_MODE, DragReleaseParams} from '@niivue/niivue';

@Component({
  selector: 'app-nifti-viewer',
  templateUrl: './nifti-viewer.component.html',
  styleUrls: ['./nifti-viewer.component.scss'],
})
export class NiftiViewerComponent implements OnInit, AfterViewInit, OnDestroy {


  @ViewChild('glCanvas') canvasRef!: ElementRef<HTMLCanvasElement>;  // Reference to canvas element
  niivue: Niivue;
  voxStart: number[] = [0, 0, 0];  // To store starting voxel coordinates
  voxEnd: number[] = [0, 0, 0];    // To store ending voxel coordinates
  isDrawing: boolean = false;       // To track if drawing is in progress
  DrawingEnabled: boolean = false;

  constructor() {
    const onDragRelease = (data: DragReleaseParams) : void => {
      this.drawRectangleNiivue(this.niivue, data);
    };
  
    this.niivue = new Niivue({
      show3Dcrosshair: true,
      dragMode: DRAG_MODE.callbackOnly,
    });
  
    this.niivue.onDragRelease = onDragRelease;
    this.niivue.drawOpacity = 1.0;
  }

  ngOnInit(): void {
    this.loadDefaultVolume();
  }

  ngAfterViewInit(): void {
    // Access the canvas from the ViewChild
    const canvas = this.canvasRef.nativeElement;
    
    // Attach Niivue to the canvas element
    this.niivue.attachToCanvas(canvas);
    this.loadDefaultVolume();
  }

  ngOnDestroy(): void {
    const canvas = this.canvasRef.nativeElement;
  }

  private loadDefaultVolume() {
    const url = './assets/sub-00078_space-orig_FLAIR.nii.gz';
    const volumes = [
      {
        url,
        schema: 'nifti',
        volume: { hdr: null, img: null },
        colorMap: 'gray',
        opacity: 0.5,
        visible: true,
      },
    ];

    this.niivue.attachTo('gl');
    this.niivue.loadVolumes(volumes)
      .then(() => {})
      .catch(err => {
        console.error("Error loading volumes:", err);
      });
  }

  public enableDrawing(): void {
    this.DrawingEnabled = true;
    console.log('Drawing mode enabled.');
  }

  public disableDrawing(): void {
    this.DrawingEnabled = false;
    console.log('Drawing mode disabled.');
  }

  private onRectangleDraw(data: any): void {
    this.drawRectangleNiivue(this.niivue, data);
  }

  private drawRectangleNiivue(nv: Niivue, data: any): void {
    if(this.DrawingEnabled){
    nv.setDrawingEnabled(true);
    const colourValue = 5;
    nv.setPenValue(colourValue);

    const { voxStart, voxEnd, axCorSag } = data;
    let topLeft: number[] = [0, 0, 0], topRight: number[] = [0, 0, 0], bottomLeft: number[] = [0, 0, 0], bottomRight: number[] = [0, 0, 0];
    let topLeftO: number[] = [0, 0, 0], topRightO: number[] = [0, 0, 0], bottomLeftO: number[] = [0, 0, 0], bottomRightO: number[] = [0, 0, 0];

    switch (axCorSag) {
      case 0: { // Coronal
        const minX = Math.min(voxStart[0], voxEnd[0]);
        const maxX = Math.max(voxStart[0], voxEnd[0]);
        const minY = Math.min(voxStart[1], voxEnd[1]);
        const maxY = Math.max(voxStart[1], voxEnd[1]);
        const fixedZ = voxStart[2];
        topLeft = [minX, minY, fixedZ];
        topRight = [maxX, minY, fixedZ];
        bottomLeft = [minX, maxY, fixedZ];
        bottomRight = [maxX, maxY, fixedZ];

        topLeftO = [minX - 1, minY - 1, fixedZ];
        topRightO = [maxX + 1, minY - 1, fixedZ];
        bottomLeftO = [minX - 1, maxY + 1, fixedZ];
        bottomRightO = [maxX + 1, maxY + 1, fixedZ];
        break;
      }
      case 1: { // Sagittal
        const minX = Math.min(voxStart[0], voxEnd[0]);
        const maxX = Math.max(voxStart[0], voxEnd[0]);
        const minZ = Math.min(voxStart[2], voxEnd[2]);
        const maxZ = Math.max(voxStart[2], voxEnd[2]);
        const fixedY = voxStart[1];
        topLeft = [minX, fixedY, minZ];
        topRight = [maxX, fixedY, minZ];
        bottomLeft = [minX, fixedY, maxZ];
        bottomRight = [maxX, fixedY, maxZ];

        topLeftO = [minX - 1, fixedY, minZ - 1];
        topRightO = [maxX + 1, fixedY, minZ - 1];
        bottomLeftO = [minX - 1, fixedY, maxZ + 1];
        bottomRightO = [maxX + 1, fixedY, maxZ + 1];
        break;
      }
      case 2: { // Axial
        const minY = Math.min(voxStart[1], voxEnd[1]);
        const maxY = Math.max(voxStart[1], voxEnd[1]);
        const minZ = Math.min(voxStart[2], voxEnd[2]);
        const maxZ = Math.max(voxStart[2], voxEnd[2]);
        const fixedX = voxStart[0];
        topLeft = [fixedX, minY, minZ];
        topRight = [fixedX, maxY, minZ];
        bottomLeft = [fixedX, minY, maxZ];
        bottomRight = [fixedX, maxY, maxZ];

        topLeftO = [fixedX, minY - 1, minZ - 1];
        topRightO = [fixedX, maxY + 1, minZ - 1];
        bottomLeftO = [fixedX, minY - 1, maxZ + 1];
        bottomRightO = [fixedX, maxY + 1, maxZ + 1];
        break;
      }
      default: {
        console.error('Invalid axCorSag value.');
        return;
      }
    }


    nv.drawPenLine(topLeft, topRight, colourValue);
    nv.drawPenLine(topRight, bottomRight, colourValue);
    nv.drawPenLine(bottomRight, bottomLeft, colourValue);
    nv.drawPenLine(bottomLeft, topLeft, colourValue);

    nv.drawPenLine(topLeftO, topRightO, colourValue);
    nv.drawPenLine(topRightO, bottomRightO, colourValue);
    nv.drawPenLine(bottomRightO, bottomLeftO, colourValue);
    nv.drawPenLine(bottomLeftO, topLeftO, colourValue);

    nv.refreshDrawing(true);
    nv.setDrawingEnabled(false);
    console.log("Drawn?")}
  }


}
