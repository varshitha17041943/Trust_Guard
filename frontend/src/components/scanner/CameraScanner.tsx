import React, { useEffect, useRef, useState } from 'react';
import { Html5Qrcode } from 'html5-qrcode';
import { Loader2, AlertTriangle } from 'lucide-react';

const CameraScanner = ({ onSuccess }: { onSuccess: (url: string) => void }) => {
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    const html5QrCode = new Html5Qrcode("qr-reader");
    
    html5QrCode.start(
      { facingMode: "environment" },
      { fps: 10, qrbox: { width: 250, height: 250 } },
      (decodedText) => {
        html5QrCode.stop();
        onSuccess(decodedText);
      },
      (err) => {
        // Ignore continuous stream errors
      }
    ).then(() => setLoading(false)).catch((err) => {
      setError("Failed to access camera. Please ensure permissions are granted.");
      setLoading(false);
    });

    return () => {
      if (html5QrCode.isScanning) {
        html5QrCode.stop().catch(() => {});
      }
    };
  }, [onSuccess]);

  return (
    <div className="w-full flex flex-col items-center">
      {error && (
        <div className="bg-danger/10 border border-danger text-danger p-4 rounded-lg mb-4 flex items-center gap-2">
          <AlertTriangle size={20} /> {error}
        </div>
      )}
      {loading && !error && (
        <div className="flex flex-col items-center justify-center p-12">
          <Loader2 className="animate-spin text-primary w-12 h-12 mb-4" />
          <p className="text-gray-400">Initializing Camera...</p>
        </div>
      )}
      <div id="qr-reader" className="w-full max-w-md overflow-hidden rounded-xl border-2 border-border shadow-2xl"></div>
    </div>
  );
};

export default CameraScanner;
