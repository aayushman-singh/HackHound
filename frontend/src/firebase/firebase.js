// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBZT3wK4oUD6zaXFIRm8A-7pA_VVkuOI7I",
  authDomain: "fuzzer-46190.firebaseapp.com",
  projectId: "fuzzer-46190",
  storageBucket: "fuzzer-46190.appspot.com",
  messagingSenderId: "1006329990110",
  appId: "1:1006329990110:web:83cbc1bddf80a3b9156b4f",
  measurementId: "G-4G8H76VK7V"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const auth = getAuth(app)
const analytics = getAnalytics(app);