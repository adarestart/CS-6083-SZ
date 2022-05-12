import React from 'react';
import axios from 'axios';
import '../App.css';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

export default class VehicleList extends React.Component {
  state = {
    vehicles: []
  }
  componentDidMount() {
    axios.get(``)
    .then(response => {
    const posts = response.data;
    this.setState ({ vehicles: posts.data});
    })
  }
  
  render() {
    console.log(this.state.vehicles);
    return (
      
      <div className="col">
        <h1>Vehicles Available</h1>
        <p>Vehicle List</p>
        <table>
          <thead>
            <tr height="60px" background="#FFED86" font-size="16px">
              <th>ID</th>
              <th>MAKE</th>
              <th>MODEL</th>
              <th>YEAR</th>
              <th>VIN</th>
              <th>LPN</th>
            </tr>
          </thead>
          <tbody height="48px" border-bottom="1px" solid="#E3F1D5">
          {this.state.vehicles.map(home => <tr><th>{home.id}</th><th>{home.make}</th><th>{home.model}</th><th>{home.make_year}</th></tr>)} 
          </tbody>
        </table>
      </div>
  
  )}
}
