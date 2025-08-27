import React from 'react';

const ContactUs = () => {
  return (
    <div className="bg-gray-800 py-16 px-8 text-white">
      <div className="container mx-auto text-center">
        <h2 className="text-4xl font-bold mb-8">Contact Us</h2>
        <p className="mb-12 text-gray-300">
          We would love to hear from you! Please fill out the form below to get in touch.
        </p>
        <form className="bg-gray-900 rounded-lg p-8 shadow-lg w-full max-w-md mx-auto">
          <div className="mb-4">
            <label className="block text-left text-gray-300 mb-2" htmlFor="name">
              Name
            </label>
            <input
              type="text"
              id="name"
              className="w-full p-2 rounded bg-gray-700 border border-gray-600 focus:outline-none focus:ring-2 focus:ring-yellow-400"
              placeholder="Your Name"
              required
            />
          </div>
          <div className="mb-4">
            <label className="block text-left text-gray-300 mb-2" htmlFor="email">
              Email
            </label>
            <input
              type="email"
              id="email"
              className="w-full p-2 rounded bg-gray-700 border border-gray-600 focus:outline-none focus:ring-2 focus:ring-yellow-400"
              placeholder="Your Email"
              required
            />
          </div>
          <div className="mb-4">
            <label className="block text-left text-gray-300 mb-2" htmlFor="message">
              Message
            </label>
            <textarea
              id="message"
              rows="4"
              className="w-full p-2 rounded bg-gray-700 border border-gray-600 focus:outline-none focus:ring-2 focus:ring-yellow-400"
              placeholder="Your Message"
              required
            ></textarea>
          </div>
          <button
            type="submit"
            className="w-full p-2 bg-yellow-400 text-gray-800 font-bold rounded hover:bg-yellow-300 transition duration-300"
          >
            Send Message
          </button>
        </form>
      </div>
    </div>
  );
};

export default ContactUs;
