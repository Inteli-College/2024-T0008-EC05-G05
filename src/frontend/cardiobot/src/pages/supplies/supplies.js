import React, { useState } from "react";
import ModalCreated from "../../components/Supplies_popup/supplie-popup.js";
import "./supplies.css";
import Sidebar from "../../components/Sidebar/Sidebar.js";
import axios from "axios";

const Supplies = () => {
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [inputValues, setInputValues] = useState(Array(8).fill(''));
  const [modalOpen, setModalOpen] = useState(Array(8).fill(false));
  const [selectedNumber, setSelectedNumber] = useState(null); // State to hold selected number

  const toggleSidebar = () => {
    setSidebarOpen(!sidebarOpen);
  };

  const openModal = (index) => {
    const newModalOpen = [...modalOpen];
    newModalOpen[index] = true;
    setModalOpen(newModalOpen);
  };

  const closeModal = (index) => {
    const newModalOpen = [...modalOpen];
    newModalOpen[index] = false;
    setModalOpen(newModalOpen);
  };

  const handleInputChange = (value, index) => {
    const newInputValues = [...inputValues];
    newInputValues[index] = value;
    setInputValues(newInputValues);
  };

  const handleDropdownChange = (event, index) => {
    const selected = event.target.value;
    setInputValues(prevInputValues => {
      const newInputValues = [...prevInputValues];
      newInputValues[index] = selected;
      return newInputValues;
    });
  };

  // Essa é a função que envia os dados para o backend 
  const sendValues = () => {
    console.log(inputValues);
    axios.post('http://localhost:8000/posts/', {
      nome_kit : 'Kit 1',
      id_kit : 1,
      item_1 : inputValues
    })
      .then((response) => {
        console.log(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  const fetchItems = () => {
    try { 
      const items = axios.get('http://localhost:8000/posts/${id}');
      console.log(items);
    }
    catch (error) {
      console.log("error : ", error);
    }
  }

  const options = [
    ['Curativo adesivo', 'Vazio'],
    ['Pinça', 'Vazio'],
    ['Solução salina', 'Vazio'],
    ['Luva de cirurgia', 'Vazio'],
    ['Gaze estéril', 'Vazio'],
    ['Antisséptico', 'Vazio'],
    ['Seringa descartável', 'Vazio'],
    ['Máscara N95', 'Vazio']
  ];


  return (
    <div className="Container">
      <Sidebar open={sidebarOpen} toggleSidebar={toggleSidebar} />
      {/* Escolhe o número do kit:  */}
      <select value={selectedNumber} onChange={(event) => setSelectedNumber(event.target.value)}>
        <option value="">Select a number</option>
        {[1, 2, 3, 4, 5].map((number) => (
          <option key={number} value={number}>{number}</option>
        ))}
      </select>
      <button onClick={() => fetchItems(selectedNumber)}>Show inventory</button>
      <div className="Row">
        {[0, 1, 2, 3].map((index) => (
          <div key={index} className="Item">
            <div className="ButtonContainer">
              <button id="home_button" ></button>
            </div>
            <ModalCreated
              isOpen={modalOpen[index]}
              onRequestClose={() => closeModal(index)}
              className="modal"
              overlayClassName="overlay"
              placeholder="Enter something"
              inputValue={inputValues[index]}
              onInputChange={(value) => handleInputChange(value, index)}
            />
            <select value={inputValues[index]} onChange={(event) => handleDropdownChange(event, index)}>
              <option></option>
              {options[index].map((option, i) => (
                <option key={i} value={option}>{option}</option>
              ))}
            </select>
            <p id="individual_name" key={index}>{inputValues[index]}</p>
          </div>
        ))}
      </div>
      <div className="Row">
        {[4, 5, 6, 7].map((index) => (
          <div key={index} className="Item">
            <div className="ButtonContainer">
              <button id="home_button" ></button>
            </div>
            <ModalCreated
              isOpen={modalOpen[index]}
              onRequestClose={() => closeModal(index)}
              className="modal"
              overlayClassName="overlay"
              placeholder="Enter something"
              inputValue={inputValues[index]}
              onInputChange={(value) => handleInputChange(value, index)}
            />
            <select value={inputValues[index]} onChange={(event) => handleDropdownChange(event, index)}>
              <option></option>
              {options[index].map((option, i) => (
                <option key={i} value={option}>{option}</option>
              ))}
            </select>
            <p id="individual_name" key={index}>{inputValues[index]}</p>
          </div>
        ))}
      </div>
      <div>
        <button onClick={sendValues}>Enviar dados</button>
      </div>
    </div>
  );
};

export default Supplies;
