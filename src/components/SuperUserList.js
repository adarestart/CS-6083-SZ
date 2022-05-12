import React from 'react';
import axios from 'axios';
import { Card,Container, Table,Button, Breadcrumb,ButtonGroup} from 'react-bootstrap';
import { Row } from 'react-bootstrap';
import moment from 'moment';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

//var randomstring = require("randomstring");
export default class SuperUserList extends React.Component {

  state = {
    data_list:[],
    post_list:[],
    show_table:false,
    detail_table:false,
    put_data: null,
    url:``,

    
  }

  componentDidMount() {

  }
  

  getDataList = (url) => {
    if (url) {
      axios
        .get(url)
        .then(response => {
        const posts = response.data; 
        this.setState ({ url: url});
        this.setState ({ data_list: posts.data});
        })
    }
  };
  getUrls = event => {
    this.setState({show_table:true});
    var url = ``;
    switch(event.target.value){
      case "vehicles": url=`/api/vehicles/vehicle/`;break;
      case "offices": url=`/api/vehicles/office/`;break;
      case "classes": url=`/api/vehicles/class/`;break;
      case "orders": url=`/api/orders/`;break;
      case "payments": url=`/api/orders/payment/`;break;
      case "invoices": url=`/api/orders/invoice/`;
    }
    this.getDataList(url);
  }
  viewUrls = event => {
    this.setState({show_table:false});
    this.setState({detail_table:true});
    if (this.state.url) {
      axios
        .get(this.state.url+`${Number(event.target.id)}/`)
        .then(response => {
        const posts = response.data; 
        console.log(response.data)
        this.setState ({ data_list: posts.data});
        })
    }

  }
  deleteUrls = event => {

    if (this.state.url) {
      axios
        .delete(this.state.url+`${Number(event.target.id)}/`)
        .then(response => {
        console.log(response);
        console.log(response.data);
        this.getDataList(this.state.url);

        })
    }
  }
  showListTable= () =>{
    return(
      <Table striped bordered hover size="sm" margin="auto">
        <tbody>
         {this.state.data_list.map(home => <tr>{Object.keys(home).map(function(key){return <td>{home[key]}</td>})}<Button id = {home.id}  variant="secondary" onClick={this.viewUrls}>Edit</Button><Button id = {home.id}  variant="secondary" onClick={this.deleteUrls}>Delete</Button></tr>)}
        </tbody>
        </Table>
    )
  }
  showDetailTable= () =>{
    return(
      <Card style={{ width: '18rem',background: 'linear-gradient( #e1f8dc, #caf1de)'}}>
     
       <Card.Body>
         <Card.Title>Detail Information</Card.Title>
         {this.state.data_list.map(home => <form id = {home.id} onSubmit={this.handleEdit}>{Object.keys(home).map(function(key){return <label>{key}<input id ={key} type="text" name={key} value = {home[key]} /></label>})}<button type="submit">Book</button></form>)}
                
                 
        </Card.Body>
      </Card>
    )
  }

  
  render() {
    //console.log(this.state.vehicles);
    /*<Table striped bordered hover size="sm" margin="auto">
        <tbody>
         {this.state.data_list.map(home => <tr>{Object.keys(home).map(function(key){return <td>{home[key]}</td>})}<Button id = {home.id} value = "invoices" variant="secondary" onClick={this.editUrls}>Edit</Button></tr>)}
        </tbody>
        </Table>*/
    return (
      
      <div className="users">
        <ButtonGroup aria-label="Basic example">
          <Button value = "vehicles" variant="secondary" onClick={this.getUrls}>Vehicles</Button>
          <Button value = "offices" variant="secondary" onClick={this.getUrls}>Offices</Button>
          <Button value = "classes" variant="secondary" onClick={this.getUrls}>Vehicle Class</Button>
          <Button value = "orders" variant="secondary" onClick={this.getUrls}>Orders</Button>
          <Button value = "payments" variant="secondary" onClick={this.getUrls}>Payments</Button>
          <Button value = "invoices" variant="secondary" onClick={this.getUrls}>Invoices</Button>
        </ButtonGroup>
        
        {this.state.show_table?this.showListTable():null}
        {this.state.detail_table?this.showDetailTable():null}
        
       

        
        
          
      </div>
      

  )}
}
