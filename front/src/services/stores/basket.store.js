import { action, configure, observable, toJS } from 'mobx';

configure({ enforceActions: 'observed' });

class BasketStore {

    @observable
    summa = 0;

    @observable
    basket = [
        {
            name: 'Яшкино',
            type: 'Вафли',
            weight: '200 грамм',
            price: 38,
            count: 1,
            forHowMuch: 'за шт.',
            description: 'СемислойнСемислойные вафли с начинкой из натурального какао и обжаренного фундука.Семислойные вафли с начинкой из натурального какао и обжаренного фундука.Семислойные вафли с начинкой из натурального какао и обжаренного фундука.Семислойные вафли с начинкой из натурального какао и обжаренного фундука.ые вафли с начинкой из натурального какао и обжаренного фундука.'
        },
        {
            name: 'Хуяшкино',
            type: 'Вафли',
            weight: '200 грамм',
            price: 38,
            count: 1,
            forHowMuch: 'за шт.',
            description: 'Семислойные вафли с начинкой из натурального какао и обжаренного фундука.'
        },
        {
            name: 'Хуяшкино',
            type: 'Вафли',
            weight: '200 грамм',
            price: 38,
            count: 1,
            forHowMuch: 'за шт.',
            description: 'Семислойные вафли с начинкой из натурального какао и обжаренного фундука.'
        },
        {
            name: 'Хуяшкино',
            type: 'Вафли',
            weight: '200 грамм',
            price: 38,
            count: 1,
            forHowMuch: 'за шт.',
            description: 'Семислойные вафли с начинкой из натурального какао и обжаренного фундука.'
        },{
            name: 'Хуяшкино',
            type: 'Вафли',
            weight: '200 грамм',
            price: 38,
            count: 1,
            forHowMuch: 'за шт.',
            description: 'Семислойные вафли с начинкой из натурального какао и обжаренного фундука.'
        }
    ]

    constructor(rootStore) {
        this.rootStore = rootStore;
    }

    @action
    setSumma = () => {
        this.summa = 0;
        this.basket.forEach(item => this.summa += item.count * item.price);
    }

    @action
    removeFromBasket = (index) => {
        this.basket.splice(index, 1);
        this.setSumma()
    }

    @action
    addProduct = (index) => {
        const count = this.basket[index].count;
        if (count < 999) {
            this.basket[index].count++;
            this.setSumma()
        }
    }

    @action
    reduceProduct = (index) => {
        const count = this.basket[index].count;
        if (count > 1) {
            this.basket[index].count--;
        } else {
            this.removeFromBasket(index);
        }
        this.setSumma()
    }
}

export default BasketStore;
