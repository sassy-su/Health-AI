import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import NavBar from './Nav';
import ContentSection from './HomeBody';
import AboutSection from './About';
import TeamSection from './Team';
import ReviewSection from './Review';
import ContactUs from './Contactus';
import Footer from './Footer';

const App = () => {
  return (
    <Router>
      <div>
        <NavBar />
        <div id="home">
          <ContentSection />
        </div>
        <div id="about">
          <AboutSection />
        </div>
        <div id="team">
          <TeamSection />
        </div>
        <div id="services">
          <ReviewSection />
        </div>
        <div id="contact">
          <ContactUs />
        </div>
        <Routes>
          {/* Other routes if necessary */}
        </Routes>
        <Footer />
      </div>
    </Router>
  );
};

export default App;
