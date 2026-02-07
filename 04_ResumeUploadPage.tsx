import React from 'react';

const ResumeUploadPage = ({ navigateTo, updateAppState }: any) => {
  const uploadResume = () => {
    updateAppState({
      hasResume: true,
      completedSteps: { resume: true },
    });
    navigateTo('dashboard');
  };

  return (
    <div className="p-6">
      <h2 className="text-xl mb-4">Upload Resume</h2>
      <button
        onClick={uploadResume}
        className="px-4 py-2 bg-blue-600 text-white rounded"
      >
        Upload
      </button>
    </div>
  );
};

export default ResumeUploadPage;
