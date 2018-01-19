import React , {Component} from 'react'
import { Link } from 'react-router-dom'
import { Button } from 'react-bootstrap'
import { connect } from 'react-redux';

import * as commonActions from '../constants/commonActions'

import './homePage.css'

class HomePage extends Component {

    constructor(){
      super()

      this.state = {
        roleTitle: "",
        roleLevel: "",
        industryExpetise : "",
        technologyExpetise : "",
        gallup : "",
        certifications : ""
      }

      this.onButtonClick = this.onButtonClick.bind(this);
      this.onFormUpdate = this.onFormUpdate.bind(this);
    }

    onFormUpdate(evt){
      name = evt.target.id
      this.setState({[name]:evt.target.value })
    }

    onButtonClick(){
      this.props.submitDetails(
        this.state.roleTitle,
        this.state.roleLevel,
        this.state.industryExpetise,
        this.state.technologyExpetise,
        this.state.gallup,
        this.state.certifications
      )
    }

    render(){
        return (
          <div>
            <div className="row">
              <div className="col-md-8 col-md-offset-2">
                <h1>Candidate Finder</h1>
                <p>Please complete the following form. Suggestions for the role attributes will auto-populate upon completing the role and title level.</p>
                <div className="col-md-8 col-md-offset-2">
                  <hr className="home_page_hr"/>
                  <div className="form-group">
                    <label htmlFor="roleTitle">Role Title:</label>
                    <input type="text" className="form-control" id="roleTitle" onChange={(evt) => this.onFormUpdate(evt)}/>
                  </div>
                  <div className="form-group">
                    <label htmlFor="roleLevel">Level:</label>
                    <input type="password" className="form-control" id="roleLevel" onChange={(evt) => this.onFormUpdate(evt)}/>
                  </div>
                  <hr className="home_page_hr"/>
                  <div className="form-group">
                    <label htmlFor="industryExpetise">Industry Expertise:</label>
                    <select className="form-control" id="industryExpetise" onChange={(evt) => this.onFormUpdate(evt)}>
                      <option value="" defaultValue disabled hidden>Choose here</option>
                      <option>SAP</option>
                      <option>Hanna</option>
                      <option>Something Else</option>
                    </select>
                  </div>
                  <div className="form-group">
                    <label htmlFor="technologyExpetise">Technology Expertise:</label>
                    <select className="form-control" id="technologyExpetise" onChange={(evt) => this.onFormUpdate(evt)}>
                      <option value="" defaultValue disabled hidden>Choose here</option>
                      <option>Java</option>
                      <option>HTML</option>
                      <option>Python</option>
                    </select>
                  </div>
                  <div className="form-group">
                    <label htmlFor="gallup">GALLUP Strength:</label>
                    <select className="form-control" id="gallup" onChange={(evt) => this.onFormUpdate(evt)}>
                      <option value="" defaultValue disabled hidden>Choose here</option>
                      <option>People Person</option>
                      <option>Go Getter</option>
                      <option>Smart Cookie</option>
                    </select>
                  </div>
                  <div className="form-group">
                    <label htmlFor="certifications">Certifications:</label>
                    <select className="form-control" id="certifications" onChange={(evt) => this.onFormUpdate(evt)}>
                      <option value="" defaultValue disabled hidden>Choose here</option>
                      <option>Spark Certi</option>
                      <option>Hadoop Certi</option>
                      <option>Java Certi</option>
                    </select>
                  </div>
                  <hr className="home_page_hr"/>
                 </div>
              </div>
            </div>
            <br />
            <div className="row">
              <div className="col-md-6 col-md-offset-3">
                <Button bsStyle="primary" id="submit_button" onClick={() => this.onButtonClick()}>Find Candidate</Button>
              </div>
            </div>
          </div>
        )
    }
};

const mapStateToProps = (state, ownProps) => {
  return {
    subitted: null
  }
}

function mapDispatchToProps(dispatch){
  return {
      submitDetails: (roleTitle, roleLevel, industryExpetise, technologyExpetise, gallup, certifications) => dispatch(commonActions.submitDetails(roleTitle, roleLevel, industryExpetise, technologyExpetise, gallup, certifications))
  };
}

export default  connect(mapStateToProps, mapDispatchToProps)(HomePage);
