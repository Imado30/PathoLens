import { Component, AfterViewInit, HostListener, ElementRef, ViewChild } from '@angular/core';
import { NiftiViewerComponent } from "./nifti-viewer/nifti-viewer.component";

@Component({
  selector: 'app-root',
  imports: [NiftiViewerComponent],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements AfterViewInit {
  title = 'fcd-assistant';

  // Reference to the canvas element
  @ViewChild('glCanvas') canvasRef!: ElementRef<HTMLCanvasElement>;
  @ViewChild(NiftiViewerComponent) niftiViewerComponent!: NiftiViewerComponent; // Reference to the child component

  ngAfterViewInit(): void {
    this.resizeCanvas(); 
  }

  @HostListener('window:resize', ['$event'])
  onResize() {
    this.resizeCanvas();
  }

  onDrawBorderClicked() {
    this.niftiViewerComponent.drawBorderRectangle();
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
