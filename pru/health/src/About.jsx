import React from 'react';

const AboutSection = () => {
  return (
    <div className="bg-indigo-200 py-16 px-8">
      <div className="container mx-auto text-center">
        <h2 className="text-4xl font-bold text-indigo-900 mb-8">About Us</h2>
        <p className="text-xl text-gray-800 leading-relaxed max-w-4xl mx-auto">
          We are dedicated to promoting health and wellness through advanced AI technologies. Our goal is to make healthcare accessible and proactive, empowering people to monitor their well-being effortlessly.
          <br /><br />
          At AI Health Monitor, we believe that preventive health measures are the key to a better quality of life. Join us on this journey to make health a top priority, using state-of-the-art technology and data-driven insights.
        </p>
      </div>
      <div className="video-container ">
        <iframe
          className='mx-auto'
          width="50%"
          height="400"
          src="https://www.youtube.com/embed/S7lq8N122Hg?si=W4QaYAW6YON0BfWU&autoplay=1&controls=0&modestbranding=1&fs=0&showinfo=0&rel=0&iv_load_policy=3"
          title="YouTube video player"
          frameBorder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowFullScreen
        ></iframe>
        
      </div>
    </div>
  );
};

export default AboutSection;
