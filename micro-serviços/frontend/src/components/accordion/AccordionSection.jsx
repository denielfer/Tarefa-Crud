// Este file foi feito apartir de leves modificações encima do arquivo pego pego em: 
// https://www.digitalocean.com/community/tutorials/react-react-accordion-component
// , feito por joshtronic, August 27, 2021, Acesso: 23/01/2024

import React from 'react';
import PropTypes from 'prop-types';
import './style.css'

class AccordionSection extends React.Component {
  static propTypes = {
    children: PropTypes.instanceOf(Object).isRequired,
    isOpen: PropTypes.bool.isRequired,
    label: PropTypes.string.isRequired,
    onClick: PropTypes.func.isRequired,
  };

  onClick = () => {
    this.props.onClick(this.props.label);
  };

  render() {
    const {
      onClick,
      props: { isOpen, label },
    } = this;

    return (
      <div className='header-accordion' style={{ border: '2px inset'}}
      >
        <div onClick={onClick} style={{userSelect:'none'}} className='clickable' >
          {label}
          <div style={{alignContent:'right'}}>
          </div>
        </div>
        {isOpen && (
          <div class='body-accordion'
            style={{backgroundColor: 'rgba(0, 0, 0, 0.7)'}}
          >
            {this.props.children}
          </div>
        )}
      </div>
    );
  }
}

export default AccordionSection;