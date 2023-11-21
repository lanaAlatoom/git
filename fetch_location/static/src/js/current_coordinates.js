/** @odoo-module */

import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl";

class WidgetCoordinates extends Component {
    onButtonClick() {
        var self = this;
        var is_today = this.record.data.is_today;
        if (is_today != false && navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
                self.record.update({
                    provider_latitude: position.coords.latitude,
                    provider_longitude: position.coords.longitude,
                })
            });
        }else{
            alert("This event is not today so you can't CheckIn Now");
        }
    }
    get record() {
        return this.props.record;
    }
    get latitude() {
        return this.record.data.provider_latitude;
    }
    get longitude() {
        return this.record.data.provider_longitude;
    }

}

WidgetCoordinates.template = "widget_coordinates.WidgetCoordinates";

registry.category("fields").add("location_ci", WidgetCoordinates);
//view_widgets