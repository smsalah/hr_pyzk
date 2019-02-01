odoo.hr_pyzk = function(instance) {
 var ListView = instance.web.ListView;
 ListView.include({
 render_buttons: function() {

// GET BUTTON REFERENCE
 this._super.apply(this, arguments)
 if (this.$buttons) {
 var btn = this.$buttons.find('.sync_button')
 }

// PERFORM THE ACTION
 btn.on('click', this.proxy('do_sync'))

},
 do_sync: function() {
 new instance.web.Model('pyzk.machine')
 .call('create_attendance', [[]])
 .done(function(result) {
 alert('done')
 })
 }
 });
}
