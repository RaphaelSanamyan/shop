import React from 'react';
import {
  List,
  ListItem,
  ListItemIcon,
  ListItemText,
  Divider,
} from '@material-ui/core';
import StoreMallDirectoryIcon from '@material-ui/icons/StoreMallDirectory';
import ContactPhoneIcon from '@material-ui/icons/ContactPhone';
import StoreIcon from '@material-ui/icons/Store';
import LocalShippingIcon from '@material-ui/icons/LocalShipping';
import PaymentIcon from '@material-ui/icons/Payment';
import ContactSupportIcon from '@material-ui/icons/ContactSupport';

class Navigation extends React.Component {
  links = [
    { link: '/panel/projects', name: 'Каталог', icon: StoreMallDirectoryIcon },
    { link: '/panel/categories', name: 'Контакты', icon: ContactPhoneIcon },
    { link: '/panel/companies', name: 'О магазине', icon: StoreIcon },
    { link: '/panel/education', name: 'Бесплатная доставка', icon: LocalShippingIcon },
    { link: '/panel/roles', name: 'Оплата заказа', icon: PaymentIcon },
    { link: '/panel/skills', name: 'Как купить', icon: ContactSupportIcon },
  ];

  render() {
    return (
      <>
        <Divider />
        <List>
          {this.links.map((item, index) => (
            <>
            <ListItem button key={index}>
              <ListItemIcon>{<item.icon color='primary'/>}</ListItemIcon>
              <ListItemText primary={item.name} />
            </ListItem>
            <Divider />
            </>
          ))}
        </List>
      </>
    );
  }
}

export default Navigation;