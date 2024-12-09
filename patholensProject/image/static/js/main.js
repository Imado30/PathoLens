import { Niivue } from "./index.js";

document.addEventListener('DOMContentLoaded', function() {

    const nv = new Niivue();
    const canvas = document.getElementById("imageBrain");

    //function to resize the canvas field in dependency of the device
    function adjustCanvasForDPI(canvas) {
        const context = canvas.getContext('2d');
        const dpi = window.devicePixelRatio || 1;
    
        // Get the size from the canvas element from the css
        const computedStyle = getComputedStyle(canvas);
        const width = parseInt(computedStyle.getPropertyValue('width'), 10);
        const height = parseInt(computedStyle.getPropertyValue('height'), 10);
    
        // set the new width and height 
        canvas.width = width * dpi;
        canvas.height = height * dpi;
    }
    
    nv.attachToCanvas(canvas);

    adjustCanvasForDPI(canvas);

    nv.setMultiplanarPadPixels(60);

    const baseApiURL = `/image/api/getImage/${imageID}`;

    // Load FLAIR default
    let selectedFormat = "FLAIR";
    loadImage(selectedFormat);

    //function to change the picture format if the buttons are clicked
    const radioButtons = document.querySelectorAll('input[name="option"]');
    radioButtons.forEach(radio => {
        radio.addEventListener('change', (event) => {
            selectedFormat = event.target.value;
            loadImage(selectedFormat);
        });
    });

    console.log(selectedFormat)

    function loadImage(format) {
        //get the apiURL to fetch the path to the requested image
        const apiURL = `${baseApiURL}/?format=${format}`;
        console.log(`API URL: ${apiURL}`);

        //fetch the data from the given apiURL
        fetch(apiURL)
            .then(response => {
                console.log("Response status:", response.status);
                //if response not ok throw the error
                if(!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                
                console.log(response)
                return response.json();
            })
            .then(data => {
                //get the image URL with the data.path from the api
                const imageURL = `http://127.0.0.1:8000${data.path}`;
                console.log("Image URL:", imageURL);

                //load the nifti with the fetched imageURL 
                nv.loadVolumes([
                    {
                        url: imageURL,
                        schema: "nifti"
                    },
                ]);

            })
            //catch the possible error
            .catch(err => {
                console.error("Error loading NIfTI file:", err);
            });
    }

    // Drawing functions from here on

    nv.setDrawOpacity(0.65);
    
    /**
     * 
     * @param {int} mode
     * - 0 = Eraser, 4 = yellow, 6 = purple
     * @param {boolean} filled
     * True => drawn shape will be filled
     */
    function changeDrawingMode(mode, filled){
        nv.setPenValue(mode, filled);
    }

    // Pixel
    document.getElementById("selectTool").addEventListener("click", function(e){
        nv.setDrawingEnabled(true);  
        changeDrawingMode(6, false);
    });

    // disables drawing after a Pixel is marked
    document.getElementById("imageBrain").addEventListener("mouseup", disableDrawing);

    // disables drawing
    function disableDrawing(){
        nv.setDrawingEnabled(false);
    }  

    // enables erasing the drawing by clicking on eraser
    document.getElementById("eraseTool").addEventListener("click", function(e){
        nv.setDrawingEnabled(true);
        // 0 = Eraser and true => eraser is filled so a whole area can be erased
        changeDrawingMode(0, true);
    });

    // Rectangle drawing functionality
    let startPoint = null;
    let endPoint = null;

    // Mouse-Down: Set the start point of the rectangle
    canvas.addEventListener("mousedown", (event) => {
        startPoint = { x: event.offsetX, y: event.offsetY }; // Capture the starting point of the rectangle
    });

    // Mouse-Move: Render rectangle live as the mouse moves
    canvas.addEventListener("mousemove", (event) => {
        if (startPoint) {
            endPoint = { x: event.offsetX, y: event.offsetY }; // Update the end point as the mouse moves
            drawRectangle(startPoint, endPoint); // Call function to draw the rectangle live
        }
    });

    // Mouse-Up: Finalize and save the rectangle
    canvas.addEventListener("mouseup", (event) => {
        if (startPoint && endPoint) {
            saveRectangle(startPoint, endPoint); // Save the final rectangle
            startPoint = null;  // Reset start point
            endPoint = null;    // Reset end point
        }
    });

    // Function to draw the rectangle
    function drawRectangle(startPoint, endPoint) {
        const ctx = canvas.getContext("2d"); // Get the 2D canvas context
        ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear the canvas to avoid overlapping rectangles
        ctx.strokeStyle = "red";  // Rectangle color (red)
        ctx.lineWidth = 2;        // Line width for the rectangle
        const width = endPoint.x - startPoint.x;
        const height = endPoint.y - startPoint.y;
        ctx.strokeRect(startPoint.x, startPoint.y, width, height); // Draw the rectangle
    }

    // Function to save the rectangle
    function saveRectangle(startPoint, endPoint) {
        const [x1, y1] = [startPoint.x, startPoint.y];
        const [x2, y2] = [endPoint.x, endPoint.y];
        
        // Here you can store the rectangle's area in a voxel model or other data structure
        for (let x = Math.min(x1, x2); x <= Math.max(x1, x2); x++) {
            for (let y = Math.min(y1, y2); y <= Math.max(y1, y2); y++) {
                setVoxelValue(x, y, 1); // Store the value 1 at the corresponding voxel coordinates
            }
        }
    }

    // Example method to set voxel values (would need to be adapted based on your data structure)
    function setVoxelValue(x, y, value) {
        console.log(`Voxel at (${x}, ${y}) set to value ${value}`);
    }
});
