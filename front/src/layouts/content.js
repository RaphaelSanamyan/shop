import React from 'react';
import { Redirect, Route, Switch } from 'react-router-dom';
import Main from '../containers/main';
import Catalog from '../containers/catalog';
import Backet from '../containers/backet';
import { withRouter } from 'react-router';
import Constants from '../consts';
import Order from '../containers/order';
import {
    Grid,
    Box
} from '@material-ui/core';
import notFound from '../404.png';
import { inject, observer } from 'mobx-react';

@inject('store')
@observer
class Content extends React.Component {
    render() {
        const { summa } = this.props.store.basket;
        return (
            <Switch>
                <Route
                    path='/'
                    exact
                    component={Main}
                />
                <Route
                    path='/catalog'
                    exact
                    component={Catalog}
                />
                <Route
                    path='/backet'
                    exact
                    component={Backet}
                />
                <Route
                    path='/order'
                    exact
                    component={Order}
                />
                <Route
                    component={() => {
                        return (
                            <Grid container direction='column' alignItems='center'>
                                <img className='footer-img' src={notFound} alt="Logo" style={{ width: '100%', maxWidth: '600px' }} />
                                <Box className='chalk-font-35'>Страница не найдена</Box>
                            </Grid>
                        )
                    }}
                />
            </Switch>
        );
    }
}

export default withRouter(Content);
