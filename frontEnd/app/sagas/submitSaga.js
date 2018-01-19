import { call, put, apply } from 'redux-saga/effects'
import { submitDetailsApi } from '../api/submitAPIs'
import * as types from '../constants/actionTypes'

export function* submitDetals(action){
    try {
      const response =  yield call(submitDetailsApi, action);
    } catch(err) {
      console.dir(err);
    }
}
