import React, { useRef, useState } from 'react';
import { Html5Qrcode } from 'html5-qrcode';
import { UploadCloud, AlertCircle } from 'lucide-react';

const QRUploader = ({ onSuccess }: { onSuccess: (url: string) => void }) => {
  const fileInputRef = useRef<HTMLInputElement>(null);
  const [error, setError] = useState('');

  const handleFileChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      const file = e.target.files[0];
      if (file.size > 5 * 1024 * 1024) {
        setError("File exceeds 5MB limit.");
        return;
      }
      
      try {
        const html5QrCode = new Html5Qrcode("hidden-qr-reader");
        const decodedText = await html5QrCode.scanFile(file, true);
        onSuccess(decodedText);
      } catch (err) {
        setError("No valid QR code found in the image.");
      }
    }
  };

  return (
    <div className="text-center">
      {error && (
        <div className="bg-danger/10 border border-danger text-danger p-4 rounded-lg mb-4 flex justify-center items-center gap-2">
          <AlertCircle size={18} /> {error}
        </div>
      )}
      <div 
        className="border-2 border-dashed border-border hover:border-primary/50 transition bg-surface rounded-xl p-12 cursor-pointer flex flex-col items-center"
        onClick={() => fileInputRef.current?.click()}
      >
        <UploadCloud className="w-16 h-16 text-gray-500 mb-4" />
        <h3 className="text-xl font-bold mb-2">Drag & Drop Image</h3>
        <p className="text-gray-400 text-sm">Supported formats: JPEG, PNG, WebP (Max 5MB)</p>
        <input 
          type="file" 
          ref={fileInputRef} 
          className="hidden" 
          accept="image/jpeg, image/png, image/webp"
          onChange={handleFileChange}
        />
      </div>
      <div id="hidden-qr-reader" style={{ display: 'none' }}></div>
    </div>
  );
};

export default QRUploader;
