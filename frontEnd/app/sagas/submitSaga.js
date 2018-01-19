import { call, put, apply } from 'redux-saga/effects'
import { submitDetailsApi } from '../api/submitAPIs'
import * as types from '../constants/actionTypes'

export function* submitDetals(action){
    try {
      const response =  yield call(submitDetailsApi, action);
      yield put({type: types.SET_DETAILS_RESPONSE, chance: response.data});
    } catch(err) {
      console.dir(err);
    }
}
