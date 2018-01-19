import React , {Component} from 'react'
import { Link } from 'react-router-dom'
import { Button } from 'react-bootstrap'
import { connect } from 'react-redux';
import {withRouter} from "react-router-dom"

class Review extends Component {

    constructor(props){
      super(props)
      //this.percentageCalc = this.percentageCalc.bind(this);
    }

    componentDidMount() {
      console.log(this.props.chance)
    }

    percentageCalc(){
      var myPercent = "test"
      (this.props.chance == "unacc") ? percent =  "25%" : null
      (this.props.chance == "acc") ?  percent = "50%" : null
      (this.props.chance == "good") ?  percent = "75%" : null
      (this.props.chance == "vgood") ?  percent = "95%" : null
      return percent
    }

    render(){
        return (
          <div className="row">
            <div className="col-md-8 col-md-offset-2">
              <h1>Your Best Fit Candidate</h1>
              <p>{(this.props.chance != undefined || this.props.chance!= null) ? this.percentageCalc() : ""}</p>
            </div>
          </div>
        )
    }
};

const mapStateToProps = (state, ownProps) => {
  return {
    chance: state.chance
  }
}

function mapDispatchToProps(dispatch){
  return {
      submitDetails: (roleTitle, roleLevel, industryExpetise, technologyExpetise, gallup, certifications, education, years) => dispatch(commonActions.submitDetails(roleTitle, roleLevel, industryExpetise, technologyExpetise, gallup, certifications, education, years))
  };
}

export default  connect(mapStateToProps, mapDispatchToProps)(withRouter(Review));
