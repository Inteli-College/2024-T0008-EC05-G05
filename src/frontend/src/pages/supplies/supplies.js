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

  // Essa é a função que atualiza os dados para o backend 
  const sendValues = () => {
    console.log(inputValues);
    axios.put(`http://localhost:8000/posts/${selectedNumber}`, {
      nome_kit: `Kit ${selectedNumber}`,
      id_kit : selectedNumber,
      item_1 : inputValues
    })
      .then((response) => {
        console.log(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  const fetchItems = async () => {
    try {
      const response = await axios.get(`http://localhost:8000/posts/${selectedNumber}`);
      console.log(response.data.item_1); // Accessing item_1 directly
      // Update inputValues based on API response
      const newInputValues = [...inputValues];
      response.data.item_1.forEach((item, index) => {
        newInputValues[index] = item;
      });
      setInputValues(newInputValues);
      // Or if you want to open the modal for each item:
      response.data.item_1.forEach((item, index) => {
        openModal(index);
      });
    } catch (error) {
      console.log("error : ", error);
    }
  };

  const options = [
    ['Curativo adesivo', 'Vazio'],
    ['Agulha', 'Vazio'],
    ['Ampola Lidocaína', 'Vazio'],
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

      <div className="Header">
      <p>Escolha um kit</p>
      <select value={selectedNumber} onChange={(event) => setSelectedNumber(event.target.value)}>
        <option value="">Escolha um kit</option>
        {[1, 2, 3, 4, 5].map((number) => (
          <option key={number} value={number}>{number}</option>
        ))}
      </select>
      <button onClick={() => fetchItems(selectedNumber)}>Mostrar estoque</button>
      </div>
      <div className="Row">
        {[0, 1, 2, 3].map((index) => (
          <div key={index} className="Item">
            <div className="ButtonContainer">
              <button id="home_button" ></button>
            </div>
            <ModalCreated
              // isOpen={modalOpen[index]}
              // onRequestClose={() => closeModal(index)}
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
              // isOpen={modalOpen[index]}
              // onRequestClose={() => closeModal(index)}
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
        <button onClick={sendValues}>Salvar estoque</button>
      </div>
    </div>
  );
};

export default Supplies;
