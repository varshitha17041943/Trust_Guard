import React, { useEffect, useState } from 'react';

export const NotificationBell = () => {
    const [notifications, setNotifications] = useState([]);
    const [isOpen, setIsOpen] = useState(false);

    useEffect(() => {
        fetch('/api/notifications')
            .then(res => res.json())
            .then(data => setNotifications(data))
            .catch(err => console.error(err));
    }, []);

    const unreadCount = notifications.filter(n => !n.is_read).length;

    return (
        <div className="relative">
            <button 
                onClick={() => setIsOpen(!isOpen)}
                className="relative p-2 text-gray-400 hover:text-white transition"
            >
                🔔
                {unreadCount > 0 && (
                    <span className="absolute top-0 right-0 bg-red-500 text-white text-xs rounded-full h-4 w-4 flex items-center justify-center">
                        {unreadCount}
                    </span>
                )}
            </button>
            {isOpen && (
                <div className="absolute right-0 mt-2 w-80 bg-gray-900 border border-gray-700 rounded-lg shadow-xl z-50">
                    <div className="p-3 border-b border-gray-700 font-bold text-white">Notifications</div>
                    <div className="max-h-64 overflow-y-auto">
                        {notifications.map((n, i) => (
                            <div key={i} className={`p-3 border-b border-gray-800 ${!n.is_read ? 'bg-gray-800' : ''}`}>
                                <p className="text-sm text-gray-300">{n.message}</p>
                            </div>
                        ))}
                        {notifications.length === 0 && <div className="p-3 text-gray-500 text-center">No notifications</div>}
                    </div>
                </div>
            )}
        </div>
    );
};
