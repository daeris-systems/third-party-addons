odoo.define('pos_bag_charges.PosBagPopupWidget', function(require) {
    "use strict";

    const Popup = require('point_of_sale.ConfirmPopup');
    const Registries = require('point_of_sale.Registries');
    const PosComponent = require('point_of_sale.PosComponent');

    class PosBagPopupWidget extends Popup {
        constructor() {
            super(...arguments);
        }

        go_back_screen() {
            this.showScreen('ProductScreen');
            this.trigger('close-popup');
        }
        
        click_on_bag_product(event) {
            var self = this;
            var bag_id = parseInt(event.currentTarget.dataset['productId'])

            self.env.pos.get_order().add_product(self.env.pos.db.product_by_id[bag_id]);
            self.trigger('close-popup');
        }
        imageUrl(id) {
            return `/web/image?model=product.product&field=image_512&id=${id}&unique=1`;
        }
    };
    PosBagPopupWidget.template = 'PosBagPopupWidget';

    Registries.Component.add(PosBagPopupWidget);

    return PosBagPopupWidget;
});
