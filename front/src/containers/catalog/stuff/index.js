import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Typography from '@material-ui/core/Typography';
import cake from '../../../cake.jpg';
import ShoppingBasketIcon from '@material-ui/icons/ShoppingBasket';
import AddIcon from '@material-ui/icons/Add';
import InputBase from '@material-ui/core/InputBase';
import AddCircleIcon from '@material-ui/icons/AddCircle';
import RemoveCircleIcon from '@material-ui/icons/RemoveCircle';
import './stuff.css';
import {
    Grid,
    Button,
    Box,
    IconButton
} from '@material-ui/core';
import { inject, observer } from 'mobx-react';

@inject('store')
@observer
class Stuff extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            stuff: [
                {
                    name: 'Яшкино',
                    type: 'Вафли',
                    weight: '200 грамм',
                    price: 38,
                    forHowMuch: 'за шт.',
                    description: 'СемислойнСемислойные вафли с начинкой из натурального какао и обжаренного фундука.Семислойные вафли с начинкой из натурального какао и обжаренного фундука.Семислойные вафли с начинкой из натурального какао и обжаренного фундука.Семислойные вафли с начинкой из натурального какао и обжаренного фундука.ые вафли с начинкой из натурального какао и обжаренного фундука.'
                },
                {
                    name: 'Яшкино',
                    type: 'Вафли',
                    weight: '200 грамм',
                    price: 38,
                    forHowMuch: 'за шт',
                    description: 'Семислойные вафли с начинкой из натурального какао и обжаренного фундука.'
                },
                {
                    name: 'Яшкино',
                    type: 'Вафли',
                    weight: '200 грамм',
                    price: 38,
                    forHowMuch: 'за шт',
                    description: 'Семислойные вафли с начинкой из натурального какао и обжаренного фундука.'
                },
                {
                    name: 'Яшкино',
                    type: 'Вафли',
                    weight: '200 грамм',
                    price: 38,
                    forHowMuch: 'за шт',
                    description: 'Семислойные вафли с начинкой из натурального какао и обжаренного фундука.'
                },
                {
                    name: 'Яшкино',
                    type: 'Вафли',
                    weight: '200 грамм',
                    price: 38,
                    forHowMuch: 'за шт',
                    description: 'Семислойные вафли с начинкой из натурального какао и обжаренного фундука.'
                },
            ]
        };
    }

    render() {
        const { stuff } = this.state;
        const { addToBasket } = this.props.store.basket;
        return (
            <Grid container spacing={2}>
                {stuff.map((item, index) => (
                    <Grid item className='stuff-margin width-stuff'>
                        <Card >
                            <CardActionArea>
                                <CardMedia
                                    title="Contemplative Reptile"
                                    height="140"
                                >
                                    <img src={cake} className='img-width' alt="recipe thumbnail" />
                                </CardMedia>
                                <CardContent>
                                    <Typography gutterBottom variant="h5" component="h2">
                                        {`${item.name}, ${item.type}, ${item.weight}`}
                                    </Typography>
                                    <Typography variant="body2" component="p" className='content-scroll'>
                                        {item.description}
                                    </Typography>
                                </CardContent>
                            </CardActionArea>
                            <CardActions className='actions-align'>
                                <Typography variant='h6'>{`${item.price}₽ ${item.forHowMuch}`}</Typography>
                                <Button onClick={() => addToBasket(index)} color='secondary' >
                                    <AddIcon />
                                    <ShoppingBasketIcon />
                                </Button>
                            </CardActions>
                        </Card>
                    </Grid>
                ))}

            </Grid>
        );
    }
}

export default Stuff;