import './App.css';
import React, { useEffect, useState, useCallback } from 'react';
import axios from 'axios';

const App = () => {
  const [carList, setCarList] = useState([]);
  const [newMake, setNewMake] = useState('');
  const [newModel, setNewModel] = useState('');
  const [listState, setListState] = useState();

  useEffect(()=>{
    axios
      .get('/api/car')
      .then(response => {
        setCarList(response.data);
        setListState("LOADED");
      })
      .catch(error => {
        console.log(error);
      });
    },
    [listState]
  );

  const handleSubmit = useCallback(
    (event) => {
      event.preventDefault();
      const payload = `{"make":"${newMake}", "model":"${newModel}"}`;
      axios.post('/api/car', {
        data: payload,
      })
      .then(function () {
        setNewMake('');
        setNewModel('');
        setListState("UPDATED");
      })
      .catch(function (error) {
        console.log(error);
      });
    }, 
    [newMake, newModel]
  );

  const removeCar = useCallback(
    (id) => {
      axios
      .delete(`/api/car/${id}`)
      .then(() => {
        setListState("UPDATED");
      })
      .catch(error => {
        console.log(error);
      });
    },
    []
  );

  return (
    <div className="App">
      <header className="app-header">
        <div>
          <p>List of Automobiles</p>
          {carList.length > 0 ? (
          <ul>
          {carList.map(
            (car) => {
              console.log(car);
              return (
                <li key={car.id} className='Car-Row'>
                  <button onClick={() => removeCar(car.id)}>Remove</button>&nbsp;
                  Make: <span>{car.make}</span>, Model: <span>{car.model}</span>
                </li>                
              );
            }
          )}        
          </ul>
          ) : (
            <p>Empty list</p>
          )}
        </div>
        <div className='input-block'>
          <p>Add Automobile</p>
          <p>Make: <input type='text' value={newMake} id='make' onChange={(event) => setNewMake(event.target.value)}/></p>
          <p>Model: <input type='text' value={newModel} id='model' onChange={(event) => setNewModel(event.target.value)}/></p>
          <button onClick={handleSubmit}>Add</button>
        </div>
      </header>
    </div>
  );
}

export default App;