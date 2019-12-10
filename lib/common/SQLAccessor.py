import psycopg2
import psycopg2.extras
#const psql = require('pg');
#const {
#  sqlConnection,
#} = require('../../config/config');

class SQLAccessor:
  #/**
  # * Constructor
  # * @return {Any} none
  # */
  #constructor() {
  #  this.pool = new psql.Pool(sqlConnection);
  #  this.connected = this.pool.connect();
  #}
  def __init__(self):
    print("### constructor ")
    host = 'localhost'
    dbname = 'akitainu'
    user = 'postgres'
    password = 'postgres'
    port = 5432
    self.conn = psycopg2.connect(host=host, dbname=dbname, user=user, password=password, port=port)
    self.conn.autocommit = True # Trun on auto commit
    self.dictcur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) # Use dictionary type variable

    pass

  #/**
  # * Destructor
  # * @return {Any} none
  # */
  #destructor() {
  #  this.pool.close();
  #}
  def __del__(self):
    pass

  
  #/**
  # * Execute query
  # * @param {String} query query string
  # * @return {Object} result
  # */
  #async execute(query) {
  #  await this.connected;
  #  try {
  #    return this.pool.query(query);
  #  } catch (e) {
  #    throw e;
  #  }
  #}
  def execute(self, query):
    self.dictcur.execute(query)

  def fetch(self, query):
    self.dictcur.execute(query)
    return self.dictcur.fetchall()
  '''
  /**
   * @description Begin SQL transaction
   * @return {Object} transaction
   */
  async beginTransaction() {
    await this.connected;
    try {
      await this.pool.query('BEGIN');
      return;
    } catch (e) {
      throw e;
    }
  }

  /**
   * @description Commit SQL transaction
   * @param {Object} transaction transaction
   * @return {Any} none
   */
  async commitTransaction() {
    try {
      await this.pool.query('COMMIT');
    } catch (e) {
      throw e;
    }
  }

  /**
   * @description Rollback SQL transaction
   * @param {Object} transaction transaction
   * @return {Any} none
   */
  // eslint-disable-next-line class-methods-use-this
  async rollbackTransaction() {
    try {
      await this.pool.query('ROLLBACK');
      return;
    } catch (e) {
      throw e;
    }
  }

  /**
   * @description All in one executor
   * @param {String} query query string
   * @return {Object} result
   */
  async executeWithTransaction(query) {
    try {
      await this.beginTransaction();
      const result = await this.execute(query);
      await this.commitTransaction();
      return result;
    } catch (e) {
      await this.rollbackTransaction();
      throw e;
    }
  }

}

module.exports = new SQLAccessor(() => {});
'''