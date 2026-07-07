import React, { useState } from 'react';
import CameraScanner from './CameraScanner';
import QRUploader from './QRUploader';
import ExtractionResult from './ExtractionResult';
import { motion } from 'framer-motion';
import { Camera, Upload } from 'lucide-react';

const QRScanner = () => {
  const [mode, setMode] = useState<'camera' | 'upload'>('upload');
  const [extractedUrl, setExtractedUrl] = useState<string | null>(null);

  const handleSuccess = (url: string) => {
    setExtractedUrl(url);
  };

  if (extractedUrl) {
    return <ExtractionResult url={extractedUrl} onReset={() => setExtractedUrl(null)} />;
  }

  return (
    <div className="max-w-2xl mx-auto glass-panel p-8">
      <div className="flex justify-center gap-4 mb-8">
        <button 
          onClick={() => setMode('upload')} 
          className={`flex items-center gap-2 px-6 py-3 rounded-lg font-medium transition ${mode === 'upload' ? 'bg-primary text-white' : 'bg-surface text-gray-400 hover:text-white'}`}
        >
          <Upload size={20} /> Upload Image
        </button>
        <button 
          onClick={() => setMode('camera')} 
          className={`flex items-center gap-2 px-6 py-3 rounded-lg font-medium transition ${mode === 'camera' ? 'bg-primary text-white' : 'bg-surface text-gray-400 hover:text-white'}`}
        >
          <Camera size={20} /> Camera
        </button>
      </div>
      
      <motion.div 
        key={mode}
        initial={{ opacity: 0, x: mode === 'camera' ? 20 : -20 }}
        animate={{ opacity: 1, x: 0 }}
        transition={{ duration: 0.3 }}
      >
        {mode === 'camera' ? (
          <CameraScanner onSuccess={handleSuccess} />
        ) : (
          <QRUploader onSuccess={handleSuccess} />
        )}
      </motion.div>
    </div>
  );
};

export default QRScanner;
