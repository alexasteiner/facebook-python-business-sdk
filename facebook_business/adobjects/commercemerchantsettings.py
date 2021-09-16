# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from facebook_business.adobjects.abstractobject import AbstractObject
from facebook_business.adobjects.abstractcrudobject import AbstractCrudObject
from facebook_business.adobjects.objectparser import ObjectParser
from facebook_business.api import FacebookRequest
from facebook_business.typechecker import TypeChecker

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class CommerceMerchantSettings(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isCommerceMerchantSettings = True
        super(CommerceMerchantSettings, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        braintree_merchant_id = 'braintree_merchant_id'
        checkout_message = 'checkout_message'
        contact_email = 'contact_email'
        cta = 'cta'
        disable_checkout_urls = 'disable_checkout_urls'
        display_name = 'display_name'
        external_merchant_id = 'external_merchant_id'
        facebook_channel = 'facebook_channel'
        feature_eligibility = 'feature_eligibility'
        has_discount_code = 'has_discount_code'
        has_onsite_intent = 'has_onsite_intent'
        id = 'id'
        instagram_channel = 'instagram_channel'
        merchant_alert_email = 'merchant_alert_email'
        merchant_page = 'merchant_page'
        merchant_status = 'merchant_status'
        onsite_commerce_merchant = 'onsite_commerce_merchant'
        payment_provider = 'payment_provider'
        privacy_url_by_locale = 'privacy_url_by_locale'
        review_rejection_messages = 'review_rejection_messages'
        review_rejection_reasons = 'review_rejection_reasons'
        supported_card_types = 'supported_card_types'
        terms = 'terms'
        terms_url_by_locale = 'terms_url_by_locale'
        whatsapp_channel = 'whatsapp_channel'

    def api_get(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=CommerceMerchantSettings,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_acknowledge_order(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'idempotency_key': 'string',
            'orders': 'list<map>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/acknowledge_orders',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=CommerceMerchantSettings,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=CommerceMerchantSettings, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_commerce_orders(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.commerceorder import CommerceOrder
        param_types = {
            'filters': 'list<filters_enum>',
            'state': 'list<state_enum>',
            'updated_after': 'datetime',
            'updated_before': 'datetime',
        }
        enums = {
            'filters_enum': CommerceOrder.Filters.__dict__.values(),
            'state_enum': CommerceOrder.State.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/commerce_orders',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=CommerceOrder,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=CommerceOrder, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_commerce_payouts(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.commercepayout import CommercePayout
        param_types = {
            'end_time': 'datetime',
            'start_time': 'datetime',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/commerce_payouts',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=CommercePayout,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=CommercePayout, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_commerce_transactions(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.commerceordertransactiondetail import CommerceOrderTransactionDetail
        param_types = {
            'end_time': 'datetime',
            'payout_reference_id': 'string',
            'start_time': 'datetime',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/commerce_transactions',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=CommerceOrderTransactionDetail,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=CommerceOrderTransactionDetail, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_order_management_apps(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.application import Application
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/order_management_apps',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Application,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Application, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_order_management_app(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/order_management_apps',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=CommerceMerchantSettings,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=CommerceMerchantSettings, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_product_catalogs(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.productcatalog import ProductCatalog
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/product_catalogs',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductCatalog,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ProductCatalog, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_returns(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'end_time_created': 'datetime',
            'merchant_return_id': 'string',
            'start_time_created': 'datetime',
            'statuses': 'list<statuses_enum>',
        }
        enums = {
            'statuses_enum': [
                'APPROVED',
                'DISAPPROVED',
                'MERCHANT_MARKED_COMPLETED',
                'REFUNDED',
                'REQUESTED',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/returns',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_setup_status(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from facebook_business.adobjects.commercemerchantsettingssetupstatus import CommerceMerchantSettingsSetupStatus
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/setup_status',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=CommerceMerchantSettingsSetupStatus,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=CommerceMerchantSettingsSetupStatus, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_shipping_profiles(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'reference_id': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/shipping_profiles',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_shipping_profile(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'handling_time': 'map',
            'is_default_shipping_profile': 'bool',
            'name': 'string',
            'reference_id': 'string',
            'shipping_destinations': 'list<map>',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/shipping_profiles',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def get_tax_settings(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/tax_settings',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_whatsapp_channel(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from facebook_business.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'op': 'op_enum',
            'whatsapp_business_accounts': 'list<string>',
        }
        enums = {
            'op_enum': [
                'ADD',
                'REMOVE',
            ],
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/whatsapp_channel',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    _field_types = {
        'braintree_merchant_id': 'string',
        'checkout_message': 'string',
        'contact_email': 'string',
        'cta': 'string',
        'disable_checkout_urls': 'bool',
        'display_name': 'string',
        'external_merchant_id': 'string',
        'facebook_channel': 'Object',
        'feature_eligibility': 'Object',
        'has_discount_code': 'bool',
        'has_onsite_intent': 'bool',
        'id': 'string',
        'instagram_channel': 'Object',
        'merchant_alert_email': 'string',
        'merchant_page': 'Profile',
        'merchant_status': 'string',
        'onsite_commerce_merchant': 'Object',
        'payment_provider': 'string',
        'privacy_url_by_locale': 'map<string, string>',
        'review_rejection_messages': 'list<string>',
        'review_rejection_reasons': 'list<string>',
        'supported_card_types': 'list<string>',
        'terms': 'string',
        'terms_url_by_locale': 'map<string, string>',
        'whatsapp_channel': 'Object',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


