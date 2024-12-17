import { Component, OnInit } from '@angular/core';
import { Niivue } from '@niivue/niivue';

@Component({
  selector: 'app-nifti-viewer',
  templateUrl: './nifti-viewer.component.html',
  styleUrls: ['./nifti-viewer.component.scss']
})
export class NiftiViewerComponent implements OnInit {

  constructor() {}

  niivue = new Niivue({ show3Dcrosshair: true });

  ngOnInit(): void {
    const url = './assets/sub-00078_space-orig_FLAIR.nii.gz';

    const volumeList = [
      {
        url,
        schema: 'nifti',
        volume: { hdr: null, img: null },
        colorMap: 'gray',
        opacity: 1,
        visible: true
      }
    ];


    this.niivue.attachTo('gl');

    this.niivue.loadVolumes(volumeList)
      .then(() => {
      })
      .catch(err => {
        console.error("Error loading volumes:", err);
      });
  }

 
  public drawBorderRectangle(): void {
    if (!this.niivue.volumes || this.niivue.volumes.length === 0 || !this.niivue.volumes[0].dimsRAS) {
      console.error("Error: Volume data not loaded properly.");
      return;
    }

    this.niivue.setDrawingEnabled(true)

    const dims = this.niivue.volumes[0].dimsRAS; 
    if (!dims) {
      console.error("Error: Volume dimensions not available.");
      return;
    }

    console.log("Volume Dimensions (X, Y, Z):", dims);
    
    const maxX = dims[0] - 1; 
    const maxY = dims[1] - 1; 
    const fixedZ = 0;     

    const penColor = 4; 

    const topLeft = [0, 0, fixedZ];
    const topRight = [maxX, 0, fixedZ];
    const bottomLeft = [0, maxY, fixedZ];
    const bottomRight = [maxX, maxY, fixedZ];

    this.niivue.setPenValue(penColor);

    this.niivue.drawPenLine(topLeft, topRight, penColor);       // Top edge
    this.niivue.drawPenLine(topRight, bottomRight, penColor);   // Right edge
    this.niivue.drawPenLine(bottomRight, bottomLeft, penColor); // Bottom edge
    this.niivue.drawPenLine(bottomLeft, topLeft, penColor);     // Left edge

    this.niivue.refreshDrawing(true);
  }
}
