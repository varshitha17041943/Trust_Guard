import React, { useState, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import { motion } from 'framer-motion';
import { QrCode, Upload, Camera, ArrowRight } from 'lucide-react';

const QRScanner = () => {
  const [isScanning, setIsScanning] = useState(false);
  const [file, setFile] = useState<File | null>(null);
  const navigate = useNavigate();
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleSimulateScan = () => {
    setIsScanning(true);
    setTimeout(() => {
      navigate(`/app/results/mock-qr-id`);
    }, 2000);
  };

  return (
    <div className="max-w-3xl mx-auto space-y-8">
      <div className="text-center space-y-4 mb-12">
        <div className="w-16 h-16 mx-auto bg-accent/20 rounded-full flex items-center justify-center">
          <QrCode className="text-accent w-8 h-8" />
        </div>
        <h1 className="text-3xl font-bold">QR Code Scanner</h1>
        <p className="text-gray-400">Upload a QR image or use your camera to detect malicious payloads.</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <motion.div 
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
          className="glass-panel p-8 text-center flex flex-col items-center justify-center border-dashed border-2 border-border hover:border-accent/50 cursor-pointer transition-colors"
          onClick={() => fileInputRef.current?.click()}
        >
          <input 
            type="file" 
            ref={fileInputRef} 
            className="hidden"
            accept="image/*" 
            onChange={(e) => { 
              if(e.target.files && e.target.files[0]) { 
                setFile(e.target.files[0]); 
                handleSimulateScan(); 
              } 
            }}
          />
          <Upload className="w-12 h-12 text-gray-500 mb-4" />
          <h3 className="font-bold mb-2">Upload Image</h3>
          <p className="text-sm text-gray-400">Drop your QR code here or browse</p>
        </motion.div>

        <motion.div 
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ delay: 0.1 }}
          className="glass-panel p-8 text-center flex flex-col items-center justify-center hover:bg-white/5 cursor-pointer transition-colors"
          onClick={handleSimulateScan}
        >
          <Camera className="w-12 h-12 text-gray-500 mb-4" />
          <h3 className="font-bold mb-2">Use Camera</h3>
          <p className="text-sm text-gray-400">Scan directly from your device</p>
        </motion.div>
      </div>

      {isScanning && (
        <motion.div 
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className="glass-panel p-6 text-center"
        >
          <div className="animate-pulse-slow flex flex-col items-center">
            <QrCode className="text-accent w-10 h-10 mb-4 animate-bounce" />
            <p className="font-medium text-accent">Decoding and Analyzing Vector...</p>
          </div>
        </motion.div>
      )}
    </div>
  );
};

export default QRScanner;
