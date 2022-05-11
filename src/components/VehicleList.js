import React from 'react';
import axios from 'axios';
import { Card,Button} from 'react-bootstrap';
import { Row } from 'react-bootstrap';
import moment from 'moment';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

//var randomstring = require("randomstring");
export default class VehicleList extends React.Component {

  state = {
    city_value:"Los Angelos",
    vehicles: [],
    vehicle_detail:[],
    order_detail:[],
    pay_sum:[],
    invoice_detail:[],
    pay_detail:[],
    payment_choice:1,
    show_order:true,
  }

  componentDidMount() {
    console.log(this.state.city_value)
    axios.get(`/api/vehicles/`)
    .then(response => {
    console.log(response.data.data)

    const posts = response.data.data.filter(home => home.city.includes(this.state.city_value));
    console.log(posts);
    //this.setState ({ vehicles: posts.data});
    this.setState ({ vehicles: posts});
    this.setState ({ vehicle_detail:[]});
    })
  }
  refreshList(){
    //console.log(this.state.city_value);
    axios.get(`/api/vehicles/`)
    .then(response => {
    console.log(response.data.data)
    //console.log(this.state.city_value)

    const posts = response.data.data.filter(home => home.city.includes(this.state.city_value));
    console.log(posts);
    //this.setState ({ vehicles: posts.data});
    this.setState ({ vehicles: posts});
    this.setState ({ vehicle_detail:[]});
    })

  }

  handleSubmit = (id) => {

    if (id) {
      axios
        .get(`/api/vehicles/${id}/`)
        .then(response => {
        const posts = response.data; 
        this.setState ({ vehicle_detail: posts.data});
        this.setState ({ vehicles: []});
        
        })
    }
  };
  handleChoice = event => {
    console.log(event.target.value);
    this.setState({ payment_choice: event.target.value });
    console.log(this.state.payment_choice);
  }
  handleCard = event => {
    this.setState({ card_no: event.target.value });
  }
  
  handleStart = event => {
    this.setState({ start_date: event.target.value });
  }
  handleEnd = event => {
    this.setState({ end_date: event.target.value });
  }
  handleCity = event => {
    console.log(event.target.value)
    this.setState({city_value: event.target.value});
    console.log(this.state.city_value)
  
  }
  handleOrder = event => {
    event.preventDefault();
    const date1 = moment(this.state.start_date);
    const date2 = moment(this.state.end_date);
    const date_diff = moment(date2).diff(date1, 'days')
    console.log(date_diff)
    console.log(event.target.name)
    axios.post(`/api/orders/`, {
      id:1,
      cust_id : 1,
      vehicle_id : event.target.id,
      pickup_id : '0000000009',
      dropoff_id : '0000000009',
      pickup_date: this.state.start_date,
      dropoff_date: this.state.end_date,
      start_odo: 0,
      end_odo: 0,
      odo_limit:10,
      amount:event.target.name*date_diff,
    })
      .then(res => {
        const posts = res.data;
        this.setState ({ order_detail: [posts]});
        console.log(this.state.order_detail);
        this.setState ({ vehicle_detail:[]});
        console.log(res);
        console.log(res.data);
      })
  }
  handleInvoice = event => {
    event.preventDefault();
    const date1 = moment().format('YYYY-MM-DD');
    console.log(date1)
    axios.post(`/api/orders/invoice/`, {
      id:1,
      order_id : event.target.id,
      invoice_date:date1,
      amount:event.target.name,
    })
      .then(res => {
        const posts = res.data;
        this.setState ({ invoice_detail: [posts]});
        this.setState ({ order_detail:[]});
        this.handlePayment(res.data.id,res.data.amount);
        console.log(res);
        console.log(res.data);
      })
  }
  handlePayment = (invoice,pay_amount) => {
    
    const date1 = moment().format('YYYY-MM-DD');
    console.log(date1)
    axios.post(`/api/orders/payment/`, {
      id:1,
      invoice_id : invoice,
      pay_method:Number(this.state.payment_choice),
      cardno:this.state.card_no,
      pay_date:date1,
      amount:pay_amount,
    })
      .then(res => {
      const posts = res.data;
      this.setState ({ pay_detail: posts});
      console.log(res);
      console.log(res.data);
      })
  }
  changeVehicle = (vehicle_id) => {
    
    /* NOT Finished)*/
    axios.post(`/api/orders/payment/`, {
      id:1,
    })
      .then(res => {
      console.log(res);
      console.log(res.data);
      })
  }
  
  render() {
    console.log(this.state.vehicles);
    return (
      
      <div className="vehicles">
        <h1>Vehicles Available</h1>
        
        <label>Search the city:
              <input type="text" name="City" onChange={this.handleCity.bind(this)}/>
          </label> 
          <Button  variant="secondary" onClick={this.refreshList.bind(this)}>Search</Button>
              
     
          
        <p>Vehicle List</p>
        <Row className="justify-content-center" md="auto">
        {this.state.vehicles.map(home => <Card style={{ width: '16rem',background: 'linear-gradient( #e1f8dc, #caf1de)'}}><Card.Body><Card.Title>{home.make} {home.model}</Card.Title><Card.Subtitle className="mb-2 text-muted">{home.make_year}</Card.Subtitle>
            <Card.Text>
              VIN Number: {home.VIN}          LPN Number: {home.LPN}</Card.Text>
              <Button id={home.id} variant="secondary" onClick={() => this.handleSubmit(home.id)}>View</Button>
              
          </Card.Body>
        </Card>)}
        </Row>


        <h1>View Vehicle</h1>
        <p>Vehicle Detail</p>
          <Row className="justify-content-center" md="auto">
          {this.state.vehicle_detail.map(home => <Card style={{ width: '16rem',background: 'linear-gradient( #e1f8dc, #caf1de)'}}><Card.Body><Card.Title>{home.make} {home.model}</Card.Title><Card.Subtitle className="mb-2 text-muted">{home.make_year}</Card.Subtitle>
              <Card.Text>
                VIN Number: {home.VIN}          LPN Number: {home.LPN}</Card.Text>
                <Card.Text>
                Class: {home.class_type}  </Card.Text>
                <Card.Text>
                Daily Rate: {home.daily_rate}  </Card.Text>
                <Card.Text> Extra Rate: {home.extra_rate}  </Card.Text>
                <form id = {home.id} name={home.daily_rate} onSubmit={this.handleOrder}>
                  <label>Start date
                    <input type="text" name="start_date" onChange={this.handleStart} />
                  </label>
                  <label>End date
                    <input type="text" name="end_date" onChange={this.handleEnd} />
                  </label>

                  <button type="submit">Book</button>
                </form>
            </Card.Body>
          </Card>)}
          </Row>
          
          <h1>View Order</h1>
          <p>Order Detail</p>
          <Row className="justify-content-center" md="auto">
          {this.state.order_detail.map(home => <Card style={{ width: '16rem',background: 'linear-gradient( #e1f8dc, #caf1de)'}}>
            <Card.Body>
              <Card.Title>{home.cust_id}</Card.Title>
              <Card.Subtitle className="mb-2 text-muted">{home.make_year}</Card.Subtitle>
              <Card.Text>Amount: $ {home.amount}</Card.Text>
                <Card.Text>Pick up ID: {home.pickup_id}</Card.Text>
                <Card.Text>Drop off ID: {home.dropoff_id}</Card.Text>
                <Card.Text>Pick up date: {home.pickup_date}  </Card.Text>
                <Card.Text>Drop off date: {home.dropoff_date}  </Card.Text>
                <Card.Text>Start Odometer: {home.start_odo}  </Card.Text>
                <Card.Text>Odometer Limit: {home.odo_limit}  </Card.Text>
                <form id = {home.id} name={home.amount} onSubmit={this.handleInvoice}>
                <label>
                  Pick your Payment Method:
                  <select onChange={this.handleChoice}>
                    <option value="1">Credit Card</option>
                    <option value="2">Debit Card</option>
                  </select>
                </label>
                  <label>Card Number
                    <input type="text" name="end_date" onChange={this.handleCard} />
                  </label>

                  <button type="submit">Make a Payment Right Now</button>
                </form>
            </Card.Body>
          </Card>)}
          </Row>

          <h1>View Invoice</h1>
          <p>Invoice Detail</p>
          <Row className="justify-content-center" md="auto">
          {this.state.invoice_detail.map(home => 
          <Card id={home.id} style={{ width: '16rem',background: 'linear-gradient( #e1f8dc, #caf1de)'}}>
            <Card.Body>
              <Card.Title>Invoice ID: {home.id} </Card.Title>
              <Card.Subtitle className="mb-2 text-muted">Order #{home.order_id}</Card.Subtitle>
              <Card.Text>Invoice date: {home.invoice_date} </Card.Text>
              <Card.Text> Invoice Amount: {home.amount}</Card.Text>
              <Card.Text>You payment is successful</Card.Text>
              <Button id={home.id} variant="secondary" onClick={() => this.refreshList()}>Back</Button>
            </Card.Body>
          </Card>)}
          </Row>
          
        
          
      </div>
      

  )}
}
