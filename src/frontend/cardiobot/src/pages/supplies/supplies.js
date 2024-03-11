import React, { useState } from "react";
import ModalCreated from "../../components/Supplies_popup/supplie-popup.js";
import "./supplies.css";
import Sidebar from "../../components/Sidebar/Sidebar.js";

const Supplies = () => {
  // State for sidebar
  const [sidebarOpen, setSidebarOpen] = useState(false);

  // State to manage input field values for each modal
  const [inputValues, setInputValues] = useState(Array(8).fill(''));

  // State for modals
  const [modalOpen, setModalOpen] = useState(Array(8).fill(false));

  // Function to toggle sidebar
  const toggleSidebar = () => {
    setSidebarOpen(!sidebarOpen);
  };

  // Function to open a specific modal
  const openModal = (index) => {
    const newModalOpen = [...modalOpen];
    newModalOpen[index] = true;
    setModalOpen(newModalOpen);
  };

  // Function to close a specific modal
  const closeModal = (index) => {
    const newModalOpen = [...modalOpen];
    newModalOpen[index] = false;
    setModalOpen(newModalOpen);
  };

  // Function to handle input value change for a specific modal
  const handleInputChange = (value, index) => {
    const newInputValues = [...inputValues];
    newInputValues[index] = value;
    setInputValues(newInputValues);
  };

  return (
    <div className="Container">
      {/* Sidebar component */}
      <Sidebar open={sidebarOpen} toggleSidebar={toggleSidebar} />
      <div className="Row">
        {[0, 1, 2, 3].map((index) => (
          <div key={index} className="Item">
            <div className="ButtonContainer">
            <button id="home_button" onClick={() => openModal(index)}></button>
            </div>
            <ModalCreated
              isOpen={modalOpen[index]} // Pass the modal state value here
              onRequestClose={() => closeModal(index)} // Pass the function to close the modal
              className="modal"
              overlayClassName="overlay"
              placeholder="Enter something" // Placeholder for input field
              inputValue={inputValues[index]} // Pass the input value to the modal
              onInputChange={(value) => handleInputChange(value, index)} // Pass function to handle input change
            />
            <p id="indivudual_name" key={index}>{inputValues[index]}</p>
          </div>
          
        ))}
      </div>
      <div className="Row">
        {[4, 5, 6, 7].map((index) => (
          <div key={index} className="Item">
          <div className="ButtonContainer">
          <button id="home_button" onClick={() => openModal(index)}></button>
          </div>
          <ModalCreated
            isOpen={modalOpen[index]} // Pass the modal state value here
            onRequestClose={() => closeModal(index)} // Pass the function to close the modal
            className="modal"
            overlayClassName="overlay"
            placeholder="Enter something" // Placeholder for input field
            inputValue={inputValues[index]} // Pass the input value to the modal
            onInputChange={(value) => handleInputChange(value, index)} // Pass function to handle input change
          />
          <p id="indivudual_name" key={index}>{inputValues[index]}</p>
        </div>
        ))}
      </div>
    </div>
  );
};

export default Supplies;
