import React , {Component} from 'react'
import { Link } from 'react-router-dom'
import { Button } from 'react-bootstrap'
import { connect } from 'react-redux';
import {withRouter} from "react-router-dom"

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
        certifications : "",
        education : "",
        years : ""
      }

      this.onButtonClick = this.onButtonClick.bind(this);
      this.onFormUpdate = this.onFormUpdate.bind(this);
    }

    componentWillReceiveProps(nextProps) {
      if (nextProps.chance != undefined || next.props != null){
        this.props.history.push({
            pathname: '/review',
            state: {
                chance: nextProps.chance
            }
        })
      }
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
        this.state.certifications,
        this.state.education,
        this.state.years,
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
                    <input type="text" className="form-control" id="roleLevel" onChange={(evt) => this.onFormUpdate(evt)}/>
                  </div>
                  <hr className="home_page_hr"/>
                  <div className="form-group">
                    <label htmlFor="industryExpetise">Industry Expertise:</label>
                    <select className="form-control" id="industryExpetise" onChange={(evt) => this.onFormUpdate(evt)}>
                      <option value="" defaultValue disabled hidden>Choose here</option>
                      <option value="1">SAP</option>
                      <option value="2">Hanna</option>
                      <option value="3">Big Data</option>
                      <option value="4">Security</option>
                    </select>
                  </div>
                  <div className="form-group">
                    <label htmlFor="technologyExpetise">Technology Expertise:</label>
                    <select className="form-control" id="technologyExpetise" onChange={(evt) => this.onFormUpdate(evt)}>
                      <option value="" defaultValue disabled hidden>Choose here</option>
                      <option value="1">Java</option>
                      <option value="2">HTML</option>
                      <option value="3">Python</option>
                      <option value="4">SQL</option>
                    </select>
                  </div>
                  <div className="form-group">
                    <label htmlFor="gallup">GALLUP Strength:</label>
                    <select className="form-control" id="gallup" onChange={(evt) => this.onFormUpdate(evt)}>
                      <option value="" defaultValue disabled hidden>Choose here</option>
                      <option value="1">People Person</option>
                      <option value="2">Go Getter</option>
                      <option value="3">Personal</option>
                      <option value="4">Kind</option>
                    </select>
                  </div>
                  <div className="form-group">
                    <label htmlFor="certifications">Certifications:</label>
                    <select className="form-control" id="certifications" onChange={(evt) => this.onFormUpdate(evt)}>
                      <option value="" defaultValue disabled hidden>Choose here</option>
                      <option value="1">Spark Certi</option>
                      <option value="2">Hadoop Certi</option>
                      <option value="3">Java Certi</option>
                    </select>
                  </div>

                  <div className="form-group">
                    <label htmlFor="years">Years at Accenture:</label>
                    <select className="form-control" id="years" onChange={(evt) => this.onFormUpdate(evt)}>
                      <option value="" defaultValue disabled hidden>Choose here</option>
                      <option value="1">1-3</option>
                      <option value="2">3-5</option>
                      <option value="3">5+</option>
                    </select>
                  </div>

                  <div className="form-group">
                    <label htmlFor="education">Education:</label>
                    <select className="form-control" id="education" onChange={(evt) => this.onFormUpdate(evt)}>
                      <option value="" defaultValue disabled hidden>Choose here</option>
                      <option value="1">Bsc</option>
                      <option value="2">Msc</option>
                      <option value="3">PHD</option>
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
  print("mapping state to props")
  print(state)
  return {
    chance: state.chance
  }
}

function mapDispatchToProps(dispatch){
  return {
      submitDetails: (roleTitle, roleLevel, industryExpetise, technologyExpetise, gallup, certifications, education, years) => dispatch(commonActions.submitDetails(roleTitle, roleLevel, industryExpetise, technologyExpetise, gallup, certifications, education, years))
  };
}

export default  connect(mapStateToProps, mapDispatchToProps)(withRouter(HomePage));
