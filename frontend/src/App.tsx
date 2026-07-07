import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import AppLayout from './layouts/AppLayout';
import WebsiteScanner from './pages/WebsiteScanner';
import QRScanner from './components/scanner/QRScanner';
import Results from './pages/Results';
import Dashboard from './pages/Dashboard';
import History from './pages/History';
import { AuthProvider, useAuth } from './contexts/AuthContext';
import Login from './pages/Login';
import Landing from './pages/Landing';
import Settings from './pages/Settings';
import Profile from './pages/Profile';

const ProtectedRoute = ({ children }: { children: React.ReactNode }) => {
  const { user, loading } = useAuth();
  if (loading) return <div className="p-20 text-center">Loading...</div>;
  return user ? children : <Navigate to="/login" />;
};

function App() {
  return (
    <Router>
      <AuthProvider>
        <Routes>
          <Route path="/" element={<Landing />} />
          <Route path="/login" element={<Login />} />
          <Route path="/app" element={<ProtectedRoute><AppLayout /></ProtectedRoute>}>
            <Route index element={<Navigate to="dashboard" replace />} />
            <Route path="dashboard" element={<Dashboard />} />
            <Route path="history" element={<History />} />
            <Route path="scanner" element={<WebsiteScanner />} />
            <Route path="qr" element={<QRScanner />} />
            <Route path="results/:id" element={<Results />} />
            <Route path="settings" element={<Settings />} />
            <Route path="profile" element={<Profile />} />
          </Route>
        </Routes>
      </AuthProvider>
    </Router>
  );
}

export default App;
