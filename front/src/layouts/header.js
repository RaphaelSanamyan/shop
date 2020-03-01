import React from 'react';
import {
  Grid,
  IconButton,
  Typography
} from '@material-ui/core';
import ExitToAppIcon from '@material-ui/icons/ExitToApp';
import ShoppingBasketIcon from '@material-ui/icons/ShoppingBasket';
import logotip from '../logotip.png';
import { withRouter } from 'react-router';
import './layouts.css';
import BacketAlert from '../containers/backet.alert';


class Header extends React.Component {
  toPath = (path) => {
    this.props.history.push(path)
  }
  render() {
    return (
      <Grid container justify='space-between'>
        <img className='footer-img cursor-pointer' onClick={() => this.toPath('/')} src={logotip} alt="Logo" style={{ width: '170px' }} />
        <Grid>
          <IconButton>
            <ExitToAppIcon color='primary' />
            <Typography color='primary'>&nbsp;Войти</Typography>
          </IconButton>
          <BacketAlert/>
        </Grid>
      </Grid>
    );
  }
}

export default withRouter(Header);