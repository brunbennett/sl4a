package com.googlecode.android_scripting.custom_component.item_lists;

import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import com.googlecode.android_scripting.R;
import com.googlecode.android_scripting.interpreter.InterpreterProcess;

import java.util.List;

/**
 * Adapter for a vertically scrolling list of scripts running using RecyclerView.
 *
 * @author Miguel Palacio (palaciodelgado [at] gmail [dot] com)
 */
public class ScriptMonitorListAdapter extends RecyclerView.Adapter<ScriptMonitorListAdapter.ViewHolder> {

    static final int TYPE_LIST_ITEM = 0;
    static final int TYPE_HEADER = 1;
    static final int TYPE_FOOTER = 2;

    private List<InterpreterProcess> mProcessList;

    private ViewHolder.ClickListener clickListener;

    public ScriptMonitorListAdapter(List<InterpreterProcess> mProcessList,
                                    ViewHolder.ClickListener clickListener) {
        super();
        this.mProcessList = mProcessList;
        this.clickListener = clickListener;
    }

    // ViewHolder Inner Class.
    public static class ViewHolder extends RecyclerView.ViewHolder
            implements View.OnClickListener, View.OnLongClickListener {

        int holderId;

        TextView processName;
        TextView processUpTime;
        TextView processHost;
        TextView processId;

        View itemView;

        private ClickListener listener;

        public ViewHolder(View itemView, int viewType, ClickListener listener) {
            super(itemView);

            this.itemView = itemView;

            // Set the view according with its type.
            if (viewType == TYPE_LIST_ITEM) {
                holderId = TYPE_LIST_ITEM;

                processName = (TextView) itemView.findViewById(R.id.list_item_title);
                processUpTime = (TextView) itemView.findViewById(R.id.list_item_detail_top_right);
                processHost = (TextView) itemView.findViewById(R.id.list_item_detail_bottom_left);
                processId = (TextView) itemView.findViewById(R.id.list_item_detail_bottom_right);

                // Set click listeners for the row.
                this.listener = listener;
                itemView.setOnClickListener(this);
                itemView.setOnLongClickListener(this);
            } else if (viewType == TYPE_HEADER) {
                holderId = TYPE_HEADER;
            } else {
                holderId = TYPE_FOOTER;
            }
        }

        @Override
        public void onClick(View v) {
            // Do not consider header.
            if (listener != null) {
                listener.onListItemClick(getAdapterPosition() - 1);
            }
        }

        @Override
        public boolean onLongClick(View v) {
            // Do not consider header.
            return listener!= null && listener.onItemLongClick(getAdapterPosition() - 1);
        }

        // Interface to route back click events to Activity.
        public interface ClickListener {
            void onListItemClick(int position);
            boolean onItemLongClick(int position);
        }
    }

    // Inflate the corresponding layout.
    @Override
    public ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        final int layout;
        if (viewType == TYPE_LIST_ITEM) {
            layout = R.layout.list_item_detailed;
        } else if (viewType == TYPE_HEADER) {
            layout = R.layout.list_item_empty_8dp;
        } else {
            layout = R.layout.list_item_empty_24dp;
        }

        View v = LayoutInflater.from(parent.getContext()).inflate(layout, parent, false);
        return new ViewHolder(v, viewType, clickListener);
    }

    // This method is called when the item in a row needs to be displayed.
    @Override
    public void onBindViewHolder(ViewHolder holder, int position) {
        if (holder.holderId == TYPE_LIST_ITEM) {

            InterpreterProcess process = mProcessList.get(position - 1);

            holder.processName.setText(process.getName());
            holder.processUpTime.setText(process.getUptime());
            holder.processHost.setText(process.getHost() + ":" + process.getPort());
            holder.processId.setText("PID " + process.getPid());
        }
    }

    // Return the number of items present in the list ([header] + rows + [footer]).
    @Override
    public int getItemCount() {
        return mProcessList.size() + 2;
    }

    // Return the type of the view that is being passed.
    @Override
    public int getItemViewType(int position) {
        if (position == 0) {
            return TYPE_HEADER;
        } else if (position == getItemCount() - 1) {
            return TYPE_FOOTER;
        } else {
            return TYPE_LIST_ITEM;
        }
    }

    // mProcessList has to be set in this way since to reflect changes in ScriptProcessMonitor.
    public void setmProcessList(List<InterpreterProcess> mProcessList) {
        this.mProcessList = mProcessList;
    }
}
