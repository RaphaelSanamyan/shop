import React from 'react';
import '../catalog.css';
import {
    Grid,
    ListItem,
    List,
    ListItemText,
    Divider,
    Typography
} from '@material-ui/core';

class Categories extends React.Component {
    links = [
        { link: '/panel/projects', name: 'Сухарики и гренки'},
        { link: '/panel/categories', name: 'Печенья'},
        { link: '/panel/companies', name: 'Шоколад'},
        { link: '/panel/education', name: 'Орехи'},
        { link: '/panel/roles', name: 'Чипсы'},
        { link: '/panel/skills', name: 'Сухарики'},
        { link: '/panel/education', name: 'Мармелад'},
        { link: '/panel/roles', name: 'Драже'},
        { link: '/panel/skills', name: 'Жевательная резинка'},
        { link: '/panel/skills', name: 'Специи и пряности'},
        { link: '/panel/skills', name: 'Конфеты'},
        { link: '/panel/skills', name: 'Карамель'},
      ];
    render() {
        return (
            <Grid className='categories'>
                <List>
                    <ListItem>
                        <ListItemText><Typography variant='h5'>Категории</Typography></ListItemText>
                    </ListItem>
                    {this.links.map((item, index) => (
                        <>
                            <Divider />
                            <ListItem button key={index}>
                                <ListItemText primary={item.name} />
                            </ListItem>
                        </>
                    ))}
                </List>
            </Grid>
        );
    }
}

export default Categories;