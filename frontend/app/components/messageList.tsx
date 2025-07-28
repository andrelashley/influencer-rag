"use client"

import { useState } from "react";
import styles from "./messageList.module.css";

const MessageList = () => {
  const [imageFile, setImageFile] = useState(null);

  const sendMessage = async () => {

    const formData = new FormData();
    
    if(imageFile) {
      formData.append("file", imageFile)
    }

     const response = await fetch("http://127.0.0.1:8000/uploadfile/", {
        method: "POST",
        body: formData
      });

      setImageFile(null);
  };

  const handleImageUpload = (e: any)  => {
    const file = e.target.files[0];
    if(file) {
      setImageFile(file);
    }
  };
  
  return (
    <>
        <header>
      <h1>Hello World!!</h1>
    </header>
    <label htmlFor="image-upload" className={styles.paperclipButton}>
  📎
</label>
<input
  id="image-upload"
  type="file"
  accept="image/*"
  className={styles.inputImage}
  onChange={handleImageUpload}
/>
<button onClick={sendMessage} style={{
  padding: '8px 16px',
  backgroundColor: '#007bff',
  color: '#fff',
  border: 'none',
  borderRadius: '4px',
  cursor: 'pointer',
}}>
  Upload
</button>
    </>    
  );
};

export default MessageList;