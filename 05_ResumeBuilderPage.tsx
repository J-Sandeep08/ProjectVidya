import React from 'react';

const ResumeBuilderPage = ({ navigateTo }: any) => {
  return (
    <div className="p-6">
      <h2 className="text-xl mb-4">Resume Builder</h2>
      <button
        onClick={() => navigateTo('dashboard')}
        className="px-4 py-2 bg-green-600 text-white rounded"
      >
        Save & Go Back
      </button>
    </div>
  );
};

export default ResumeBuilderPage;
