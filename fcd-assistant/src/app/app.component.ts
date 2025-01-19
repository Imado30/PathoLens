import { Component, AfterViewInit, HostListener, ElementRef, ViewChild , NgModule } from '@angular/core';
import { NiftiViewerComponent } from "./nifti-viewer/nifti-viewer.component";
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-root',
  imports: [NiftiViewerComponent , CommonModule],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements AfterViewInit {
  title = 'fcd-assistant';

  // Reference to the canvas element
  @ViewChild('glCanvas') canvasRef!: ElementRef<HTMLCanvasElement>;
  @ViewChild(NiftiViewerComponent) niftiViewerComponent!: NiftiViewerComponent; // Reference to the child component

  buttons = [
    {icon : 'fa-solid fa-arrow-pointer'},
    {icon : 'fa-regular fa-square'}
  ]

  activeButtonIndex: number = 0;

  ngAfterViewInit(): void {
    const canvas = this.niftiViewerComponent.canvasRef.nativeElement; // Access canvas in the child component
    this.resizeCanvas(); 
  }

  @HostListener('window:resize', ['$event'])
  onResize() {
    this.resizeCanvas();
  }
 
  onBarButtonClick(index: number) {
    this.activeButtonIndex = index;

    if (this.activeButtonIndex === 0){
      this.onViewingClicked()
    } else if (this.activeButtonIndex === 1) {
      this.onDrawingClicked()
    } else {

    }

  }

  onDrawingClicked() {
    this.niftiViewerComponent.enableDrawing();
  }

  onViewingClicked(){
    this.niftiViewerComponent.disableDrawing();
  }

  onChangeViewClicked(){
    this.niftiViewerComponent.changeView();
  }

  onUndoClicked(){
    this.niftiViewerComponent.undoDraw();
  }

  onClearClicked() {
    this.niftiViewerComponent.clearDraw();
  }

  private resizeCanvas(): void {
    if (this.canvasRef) {
      const canvas = this.canvasRef.nativeElement;
      const parent = canvas.parentElement;

      if (parent) {
        const rect = parent.getBoundingClientRect();
        canvas.width = rect.width;
        canvas.height = rect.height;

        const ctx = canvas.getContext('2d');
        if (ctx) {
          ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear the canvas
        }
      }
    }
  }
}
