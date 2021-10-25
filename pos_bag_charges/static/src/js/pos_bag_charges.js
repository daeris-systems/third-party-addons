odoo.define('pos_bag_charges.PosBagWidget', function(require) {
    "use strict";

    const ProductScreen = require('point_of_sale.ProductScreen');
    const PosComponent = require('point_of_sale.PosComponent');
    const Registries = require('point_of_sale.Registries');

    // Start PosBagWidget
    class PosBagWidget extends PosComponent {
        constructor() {
            super(...arguments);
        }

        renderElement (){
            var self = this;
            var selectedOrder = self.env.pos.get_order();
            var category = self.env.pos.config.pos_bag_category_id;
            var categ = self.env.pos.db.get_product_by_category(category[0])
            var products = self.env.pos.db.get_product_by_category(category[0])[0];
            var orderlines = self.env.pos.db.get_product_by_category(category[0]);

            if (self.env.pos.db.get_product_by_category(self.env.pos.config.pos_bag_category_id[0]).length == 1) {
                selectedOrder.add_product(products);
                self.env.pos.set_order(selectedOrder);
                self.showScreen('ProductScreen');
            }else{
                self.showPopup('PosBagPopupWidget', {'orderlines': orderlines});
            }
        }
    };
    PosBagWidget.template = 'PosBagWidget';

    Registries.Component.add(PosBagWidget);

    return PosBagWidget;

});
