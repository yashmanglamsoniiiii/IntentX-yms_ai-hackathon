// // --- 3D Scene Setup ---
// const scene = new THREE.Scene();
// const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
// const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });

// renderer.setSize(window.innerWidth, window.innerHeight);
// document.getElementById('canvas-container').appendChild(renderer.domElement);

// // Create a high-tech Wireframe Sphere
// const geometry = new THREE.SphereGeometry(2, 32, 32);
// const material = new THREE.MeshBasicMaterial({ 
//     color: 0x3b82f6, 
//     wireframe: true,
//     transparent: true,
//     opacity: 0.4
// });
// const sphere = new THREE.Mesh(geometry, material);
// scene.add(sphere);

// camera.position.z = 5;

// // Animation Loop
// function animate() {
//     requestAnimationFrame(animate);
//     sphere.rotation.y += 0.003;
//     sphere.rotation.x += 0.001;
    
//     // Add a slight "breathing" effect
//     const time = Date.now() * 0.001;
//     sphere.scale.set(
//         1 + Math.sin(time) * 0.05,
//         1 + Math.sin(time) * 0.05,
//         1 + Math.sin(time) * 0.05
//     );
    
//     renderer.render(scene, camera);
// }
// animate();

// // --- Handle Window Resize ---
// window.addEventListener('resize', () => {
//     camera.aspect = window.innerWidth / window.innerHeight;
//     camera.updateProjectionMatrix();
//     renderer.setSize(window.innerWidth, window.innerHeight);
// });

// // --- API Functionality ---
// async function analyzeText() {
//     const text = document.getElementById('userInput').value;
//     const btnText = document.getElementById('btnText');
//     const loader = document.getElementById('loader');
//     const resultArea = document.getElementById('resultArea');

//     if (!text || text.length < 10) {
//         alert("Please enter a longer message for intent analysis.");
//         return;
//     }

//     // UI Loading State
//     btnText.classList.add('hidden');
//     loader.classList.remove('hidden');

//     // try {
//     //     const response = await fetch('http://127.0.0.1:8000/predict', {
//     //         method: 'POST',
//     //         headers: { 'Content-Type': 'application/json' },
//     //         body: JSON.stringify({ message: text })
//     //     });


//     // Switch between these two by commenting/uncommenting:
// // const API_BASE_URL = 'http://127.0.0.1:8000'; // 🏠 Use this for Local Testing
// // const API_BASE_URL = 'https://intentx-backend.onrender.com'; // 🚀 Use this for Live Website
// try {
//     // We use backticks (`) and ${} to combine the base URL with the /predict path
//     const response = await fetch(`${API_BASE_URL}/predict`, {
//         method: 'POST',
//         headers: { 'Content-Type': 'application/json' },
//         body: JSON.stringify({ message: text }) // Ensure 'text' matches your variable name
//     });

//     const data = await response.json();
//     // ... rest of your logic to update the sphere and result card
// } catch (error) {
//     console.error("Connection Failed:", error);
//     // Optional: Show an error message on the UI
// }


        
//         const data = await response.json();

//         // Update UI
//         resultArea.classList.remove('hidden');
//         document.getElementById('riskLevel').innerText = data.label;
//         document.getElementById('riskDescription').innerText = data.analysis;
//         document.getElementById('confValue').innerText = data.confidence;
//         document.getElementById('actorType').innerText = data.label === 'PHISHING' ? "Malicious Bot" : "N/A";

//         // // Update 3D Sphere Color based on result


//         // if (data.label === 'PHISHING') {
//         //     sphere.material.color.setHex(0xef4444); // Red
//         //     document.getElementById('resultCard').style.borderColor = '#ef4444';
//         // } else if (data.label === 'SAFE') {
//         //     sphere.material.color.setHex(0x10b981); // Green
//         //     document.getElementById('resultCard').style.borderColor = '#10b981';
//         // } else {
//         //     sphere.material.color.setHex(0xf59e0b); // Orange
//         //     document.getElementById('resultCard').style.borderColor = '#f59e0b';
//         // }


//         // --- Updated UI Feedback Logic ---
// const resultCard = document.getElementById('resultCard');

// // Clear existing colors first
// resultCard.style.boxShadow = "none";

// if (data.label === 'PHISHING') {
//     // 🔴 CRITICAL THREAT (Red)
//     sphere.material.color.setHex(0xef4444); 
//     resultCard.style.borderColor = '#ef4444';
//     resultCard.style.boxShadow = '0 0 25px rgba(239, 68, 68, 0.4)'; // Add red glow
//     document.getElementById('riskLevel').style.color = '#ef4444';
// } 
// else if (data.label === 'SUSPICIOUS') {
//     // 🟡 CAUTION (Orange/Yellow)
//     sphere.material.color.setHex(0xf59e0b); 
//     resultCard.style.borderColor = '#f59e0b';
//     resultCard.style.boxShadow = '0 0 25px rgba(245, 158, 11, 0.4)'; // Add orange glow
//     document.getElementById('riskLevel').style.color = '#f59e0b';
// } 
// else {
//     // 🟢 SECURE (Green)
//     sphere.material.color.setHex(0x10b981); 
//     resultCard.style.borderColor = '#10b981';
//     resultCard.style.boxShadow = '0 0 25px rgba(16, 185, 129, 0.4)'; // Add green glow
//     document.getElementById('riskLevel').style.color = '#10b981';
// }

//     } catch (error) {
//         console.error("Backend offline. Make sure main.py is running!");
//         alert("Error: Connection to Analysis Server failed.");
//     } finally {
//         btnText.classList.remove('hidden');
//         loader.classList.add('hidden');
//     }
// }




// --- 3D Scene Setup (STAYS EXACTLY THE SAME) ---
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });

renderer.setSize(window.innerWidth, window.innerHeight);
document.getElementById('canvas-container').appendChild(renderer.domElement);

const geometry = new THREE.SphereGeometry(2, 32, 32);
const material = new THREE.MeshBasicMaterial({ 
    color: 0x3b82f6, 
    wireframe: true,
    transparent: true,
    opacity: 0.4
});
const sphere = new THREE.Mesh(geometry, material);
scene.add(sphere);

camera.position.z = 5;

function animate() {
    requestAnimationFrame(animate);
    sphere.rotation.y += 0.003;
    sphere.rotation.x += 0.001;
    const time = Date.now() * 0.001;
    sphere.scale.set(
        1 + Math.sin(time) * 0.05,
        1 + Math.sin(time) * 0.05,
        1 + Math.sin(time) * 0.05
    );
    renderer.render(scene, camera);
}
animate();

window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});

// --- API Functionality (ONLY THIS PART CHANGED FOR VERCEL) ---

// Vercel uses the same domain, so we just use the relative path
const API_URL = '/api/predict'; 

async function analyzeText() {
    const text = document.getElementById('userInput').value;
    const btnText = document.getElementById('btnText');
    const loader = document.getElementById('loader');
    const resultArea = document.getElementById('resultArea');
    const resultCard = document.getElementById('resultCard');

    if (!text || text.length < 10) {
        alert("Please enter a longer message for intent analysis.");
        return;
    }

    // UI Loading State
    btnText.classList.add('hidden');
    loader.classList.remove('hidden');

    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: text }) 
        });

        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }

        const data = await response.json();

        // --- ALL YOUR ANIMATION & UI FEEDBACK LOGIC REMAINS THE SAME ---
        resultArea.classList.remove('hidden');
        document.getElementById('riskLevel').innerText = data.label;
        document.getElementById('riskDescription').innerText = data.analysis;
        document.getElementById('confValue').innerText = data.confidence;
        document.getElementById('actorType').innerText = data.label === 'PHISHING' ? "Malicious Bot" : "N/A";

        // Clear existing colors first
        resultCard.style.boxShadow = "none";

        if (data.label === 'PHISHING') {
            sphere.material.color.setHex(0xef4444); // 🔴 Red
            resultCard.style.borderColor = '#ef4444';
            resultCard.style.boxShadow = '0 0 25px rgba(239, 68, 68, 0.4)';
            document.getElementById('riskLevel').style.color = '#ef4444';
        } 
        else if (data.label === 'SUSPICIOUS') {
            sphere.material.color.setHex(0xf59e0b); // 🟡 Orange
            resultCard.style.borderColor = '#f59e0b';
            resultCard.style.boxShadow = '0 0 25px rgba(245, 158, 11, 0.4)';
            document.getElementById('riskLevel').style.color = '#f59e0b';
        } 
        else {
            sphere.material.color.setHex(0x10b981); // 🟢 Green
            resultCard.style.borderColor = '#10b981';
            resultCard.style.boxShadow = '0 0 25px rgba(16, 185, 129, 0.4)';
            document.getElementById('riskLevel').style.color = '#10b981';
        }

    } catch (error) {
        console.error("Connection Failed:", error);
        alert("Error: Connection to Analysis Server failed.");
    } finally {
        btnText.classList.remove('hidden');
        loader.classList.add('hidden');
    }
}