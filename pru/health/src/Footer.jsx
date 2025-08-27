import React from 'react';
import { FaFacebookF, FaTwitter, FaInstagram, FaLinkedinIn } from 'react-icons/fa';

const Footer = () => {
  return (
    <div className="bg-gray-900 py-8 text-gray-300">
      <div className="container mx-auto text-center">
        <h2 className="text-2xl font-bold mb-4">Stay Connected</h2>
        <p className="mb-4">
          Your health is our priority. Join us in making the most of it!
        </p>
        <div className="flex justify-center space-x-4 mb-4">
          <a href="#" className="hover:text-yellow-400 transition duration-300">
            <FaFacebookF className="text-xl" />
          </a>
          <a href="#" className="hover:text-yellow-400 transition duration-300">
            <FaTwitter className="text-xl" />
          </a>
          <a href="www.instagram.com" className="hover:text-yellow-400 transition duration-300">
            <FaInstagram className="text-xl" />
          </a>
          <a href="#" className="hover:text-yellow-400 transition duration-300">
            <FaLinkedinIn className="text-xl" />
          </a>
        </div>
        <div className="flex justify-center space-x-8 mb-4">
          <a href="#" className="hover:text-yellow-400 transition duration-300">
            About
          </a>
          <a href="#" className="hover:text-yellow-400 transition duration-300">
            Services
          </a>
          <a href="#" className="hover:text-yellow-400 transition duration-300">
            Contact
          </a>
        </div>
        <p className="text-sm">
          &copy; {new Date().getFullYear()} AI Health Monitor. All Rights Reserved.
        </p>
      </div>
    </div>
  );
};

export default Footer;
