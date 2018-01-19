import React , {Component} from 'react';
import './header.css'

class Header extends Component {
    render(){
        return (
          <div className="row">
            <div className="col-md-5 col-md-offset-1 page-header col-sm-5 col-sm-offset-1 col-xs-5 col-xs-offset-1" id="header_box">
              <img src={require("../Images/accenture_white.png")} id="header_image"></img>
            </div>
            <div className="col-md-5 page-header col-sm-5 col-xs-5" id="header_box">
              <h2 id="header_title">Find My Candidate<br/></h2>
            </div>
          </div>
        )
    }
};

export default Header;
