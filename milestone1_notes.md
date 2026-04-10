# AURA>ego - Milestone 1 Documentation

## Overview
Milestone 1 established the foundational prototype for the AURA>ego meditation installation. The goal was to create a simple, responsive, proof-of-concept visualizer that reacts to a single user's physical presence and movement.

## Core Features Implemented

### 1. Webcam & Pose Tracking
*   **MediaPipe Integration:** Integrated Google's MediaPipe Pose library (via CDN) to perform real-time skeletal tracking from a standard webcam feed without requiring backend processing.
*   **Movement Intensity:** Calculated a normalized scalar value (0.0 to 1.0) by tracking the weighted frame-over-frame Euclidean distance of all visible joints. This serves as the primary driver for particle reactivity.
*   **Center of Mass:** Constantly derived and updated the user's physical center of mass by averaging the X and Y coordinates of the mapped body landmarks.

### 2. Responsive Particle System
*   **p5.js Engine:** Built a custom 2D physics and rendering implementation using the p5.js library.
*   **Dynamic Spawning:** The system supports 500–1000 concurrent particles emitted directly from the user's Center of Mass. Spawning frequency is dynamically tied to the movement intensity (stillness equals gentle, slow emissions, while expansive movements trigger energetic bursts).
*   **Calculated Physics:** Particles feature a randomized ~3-second lifespan, equipped with air friction (drag), a slow upward drift (anti-gravity), and soft alpha fade-outs over time.
*   **Minimalist Aesthetic:** Drawn as simple white/gray shapes layered over a pitch-black `100vw x 100vh` (`#0a0a0a`) fullscreen canvas, adhering strictly to the proof-of-concept visual constraints.

### 3. Diagnostics & UI
*   **HUD Info Panel:** A translucent top-left overlay displaying internal engine states:
    *   Movement Intensity (0.000 to 1.000)
    *   Active Particle Count
    *   Performance FPS
*   **Skeleton Debug View:** A hidden top-right picture-in-picture window (toggled via the **`D`** key) that displays the raw webcam feed overlaid with the MediaPipe skeletal wireframe and the dynamically tracked Center of Mass point.

## Technical Details
*   **Architecture:** Delivered as a single, fully-contained HTML file (`index.html`) featuring embedded CSS and JavaScript for supreme portability and ease of testing/sharing.
*   **Performance:** Optimized using `pixelDensity(1)` and utilized fast primitive p5 rendering (`circle` with `noStroke()`) to easily sustain the target 30+ minimum FPS, even under heavy 1000-particle loads.
