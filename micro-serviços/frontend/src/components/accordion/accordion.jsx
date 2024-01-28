// Este file foi feito apartir de leves modificações encima do arquivo pego pego em: 
// https://www.digitalocean.com/community/tutorials/react-react-accordion-component
// , feito por joshtronic, August 27, 2021, Acesso: 23/01/2024

import React from 'react';
import PropTypes from 'prop-types';

import AccordionSection from './AccordionSection';

class Accordion extends React.Component {
  static propTypes = {
    children: PropTypes.instanceOf(Object).isRequired,
  };

  constructor(props) {
    super(props);

    const openSections = {};

    this.state = { openSections };
  }

  onClick = label => {
    const {
      state: { openSections },
    } = this;

    const isOpen = !!openSections[label];

    this.setState({
      openSections: {
        [label]: !isOpen
      }
    });
  };

  render() {
    const {
      onClick,
      props: { children },
      state: { openSections },
    } = this;

    return (
      <div style={{ border: '2px solid', maxWidth:'50vw', alignContent:'center',margin:'auto'}}>
        {children.map(child => (
          <AccordionSection 
            isOpen={!!openSections[child.props.label]}
            label={child.props.label}
            onClick={onClick}
          >
            {child.props.children}
          </AccordionSection>
        ))}
      </div>
    );
  }
}

export default Accordion;