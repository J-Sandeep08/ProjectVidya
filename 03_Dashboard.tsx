import React from 'react';

const Dashboard = ({ navigateTo, logout }: any) => {
  return (
    <div className="p-6 space-y-4">
      <h1 className="text-2xl font-bold">Dashboard</h1>

      <button
        onClick={() => navigateTo('resume-upload')}
        className="block px-4 py-2 bg-blue-500 text-white rounded"
      >
        Upload Resume
      </button>

      <button
        onClick={logout}
        className="block px-4 py-2 bg-red-500 text-white rounded"
      >
        Logout
      </button>
    </div>
  );
};

export default Dashboard;
