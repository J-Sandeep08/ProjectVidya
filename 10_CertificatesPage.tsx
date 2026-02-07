import React from 'react';
import { Page, AppState } from '../App';

interface Props {
  navigateTo: (page: Page) => void;
  appState: AppState;
}

export default function CertificatesPage({ navigateTo, appState }: Props) {
  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-4">Suggested Certifications</h2>

      <ul className="list-disc pl-6">
        <li>Google Career Certificates</li>
        <li>AWS Cloud Practitioner</li>
        <li>Coursera / Udemy Domain Courses</li>
      </ul>
    </div>
  );
}
