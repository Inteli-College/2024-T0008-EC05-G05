import React, { useEffect, useState } from "react";
import "./supplies.css";
import Sidebar from "../../components/Sidebar/Sidebar.js";
import axios from "axios";

const Supplies = () => {
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [inputValues, setInputValues] = useState(Array(8).fill('Vazio'));
  const [modalOpen, setModalOpen] = useState(Array(8).fill(false));
  const [selectedNumber, setSelectedNumber] = useState(null); // State to hold selected number
  const [quantities, setQuantities] = useState(Array(8).fill(1)); // State to hold quantities

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

  const togglePossui = (index) => {
    const newInputValues = [...inputValues];
    newInputValues[index] = newInputValues[index] === options[index] ? 'Vazio' : options[index];
    setInputValues(newInputValues);
  };

  const handleIncrement = (index) => {
    const newQuantities = [...quantities];
    newQuantities[index]++;
    setQuantities(newQuantities);
  };

  const handleDecrement = (index) => {
    const newQuantities = [...quantities];
    if (newQuantities[index] > 1) {
      newQuantities[index]--;
      setQuantities(newQuantities);
    }
  };

  // Essa é a função que atualiza os dados para o backend 
  const sendValues = () => {
    console.log(inputValues);
    axios.put(`http://localhost:8000/posts/${selectedNumber}`, {
      ID: selectedNumber,
      Item_SKUs: inputValues,
      Kit_assembly_positions: "frente" // replace with appropriate value
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
      // Check if response.data.item_sku exists and is an array
      if (response.data.item_sku && Array.isArray(response.data.item_sku)) {
        console.log(response.data.item_sku); // Accessing item_sku directly
        // Update inputValues based on API response
        const newInputValues = [...inputValues];
        response.data.item_sku.forEach((item, index) => {
          newInputValues[index] = item;
        });
        setInputValues(newInputValues);
        // Or if you want to open the modal for each item:
        response.data.item_sku.forEach((item, index) => {
          openModal(index);
        });
      } else {
        console.log("item_sku is not an array or doesn't exist in the response data");
      }
    } catch (error) {
      console.log("error : ", error);
    }
  };

  const options = [
    'Curativo adesivo',
    'Agulha',
    'Ampola Lidocaína',
    'Luva de cirurgia',
    'Gaze estéril',
    'Antisséptico',
    'Seringa descartável',
    'Máscara N95'
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
        {options.slice(0, 4).map((option, index) => (
          <div key={index} className="Item">
            <button onClick={() => togglePossui(index)}>
              {inputValues[index] !== 'Vazio' ? inputValues[index] : 'Vazio'}
            </button>
            {inputValues[index] !== 'Vazio' && (
            <div>
              <button onClick={() => handleDecrement(index)}>-</button>
              <span>{quantities[index]}</span>
              <button onClick={() => handleIncrement(index)}>+</button>
            </div>
          )}
          </div>
        ))}
      </div>

      <div className="Row">
        {options.slice(4).map((option, index) => (
        <div key={index + 4} className="Item">
          <button onClick={() => togglePossui(index + 4)}>
            {inputValues[index + 4] !== 'Vazio' ? inputValues[index + 4] : 'Vazio'}
          </button>
          {inputValues[index + 4] !== 'Vazio' && (
          <div>
            <button onClick={() => handleDecrement(index + 4)}>-</button>
            <span>{quantities[index + 4]}</span>
            <button onClick={() => handleIncrement(index + 4)}>+</button>
          </div>
          )}
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
