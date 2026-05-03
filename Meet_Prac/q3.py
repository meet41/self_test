Mongodb:
1) db.orders.aggregate([
  {
    $lookup: {
      from: 'users',
      localField: 'user_id',
      foreignField: 'user_id',
      as: 'User'
    }
  },
  {$unwind: '$User'},
  {
    $group: {
      _id: '$User.city',
      tot_count: {$sum: 1}
    }
  },
  {$sort: {tot_count: -1}},
  {$limit: 3},
  {
    $project: {
      _id: 0,
      city: '$_id',
      tot_count: 1
    }
  }
]);

2) db.orders.aggregate([
  {$match: {items: { $elemMatch: {price: {$gt: 100}}}
           }},
  {
    $lookup: {
      from: 'users',
      localField: 'user_id',
      foreignField: 'user_id',
      as: 'user'
    }
  },
  {$unwind: '$user'},
  {$group: {
    _id: '$user.city',
    tot_order: {$sum: 1}
  }},
  {$sort: {tot_orders: -1}},
  {$limit: 3},
  {
    $project: {
      _id: 0,
      city: '$_id',
      tot_orders: 1
    }
  }
]);